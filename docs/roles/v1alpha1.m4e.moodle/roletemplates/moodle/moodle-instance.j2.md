



# moodle-instance.j2
  
---  
```

#!/bin/bash -eu
# description: install or update moodle

usage() {
    cat 1>&2 <<EOF
Script to install moodle.

ENVIRONMENT VARS:
MOODLE_APP                              moodle source path
MOODLE_CLI_TOOLS                        moodle cli path
MOODLE_INSTALL_MEMORY_LIMIT             php memory limit when installing moodle
MOODLE_UPDATE_MEMORY_LIMIT              php memory limit when updating moodle
MOODLE_CRON_MEMORY_LIMIT                php memory limit when running moodle cron
MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT   php-fpm container check script

USAGE:
    moodle-instance [OPTIONS]

OPTIONS (check moodle httpd container):
  -i            install moodle
  -u            update moodle
  -c            run moodle cron

EXAMPLES:
    moodle-instance -i
EOF
}

MOODLE_APP=${MOODLE_APP:-{{ moodle_app }}}
MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT=${MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT:-/usr/libexec/check-container-php-moodle}
MOODLE_CLI_TOOLS=${MOODLE_CLI_TOOLS:-{{ moodle_scripts_path }}}
MOODLE_INSTALL_MEMORY_LIMIT=${MOODLE_INSTALL_MEMORY_LIMIT:-{{ moodle_new_instance_job_php_max_memory }}}
MOODLE_UPDATE_MEMORY_LIMIT=${MOODLE_UPDATE_MEMORY_LIMIT:-{{ moodle_update_job_php_max_memory }}}
MOODLE_CRON_MEMORY_LIMIT=${MOODLE_CRON_MEMORY_LIMIT:-{{ moodle_cronjob_php_max_memory }}}
database_check_exit_code=""
install_check_exit_code=""

database_check() {
    echo "Checking moodle database..."
    test -f ${MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT} || { echo "${MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT} file does not exists"; exit 1; }
    database_check_exit_code=$(${MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT} -d &>/dev/null; echo $?)
}

database_check_with_retry() {
    DATABASE_CHECK_TIMES=${1:-5}
    DATABASE_CHECK_SLEEP=${2:-5}
    echo "Checking if database engine is available with ${DATABASE_CHECK_TIMES} retries and ${DATABASE_CHECK_SLEEP} seconds sleep..."

    until [ "${DATABASE_CHECK_TIMES}" -lt 0 ]; do
        database_check
        [ "${database_check_exit_code}" -eq 0 ] && return 0
        echo "Waiting for database to be available: ${DATABASE_CHECK_TIMES}..."
        sleep "${DATABASE_CHECK_SLEEP}"
        (( DATABASE_CHECK_TIMES-- ))
    done

    echo "Error: timeout waiting for database to be available, exit code: ${database_check_exit_code}"
    exit "${database_check_exit_code}"
}

install_check() {
    echo "Checking if moodle install..."
    test -f ${MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT} || { echo "${MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT} file does not exists"; exit 1; }
    install_check_exit_code=$(${MOODLE_PHP_FPM_CHECK_CONTAINER_SCRIPT} -i &>/dev/null; echo $?)
}

moodle_install() {
    echo "Installing moodle${MOODLE_INSTALL_MEMORY_LIMIT:+ with a memory limit of '${MOODLE_INSTALL_MEMORY_LIMIT}'}..."
    php ${MOODLE_INSTALL_MEMORY_LIMIT:+-d memory_limit=${MOODLE_INSTALL_MEMORY_LIMIT}} ${MOODLE_APP}/admin/cli/install_database.php \
        --lang='{{ moodle_new_instance_lang }}' \
        --fullname='{{ moodle_new_instance_fullname }}' \
        --shortname='{{ moodle_new_instance_shortname }}' \
        --summary='{{ moodle_new_instance_summary }}' \
        --adminuser='{{ moodle_new_instance_adminuser }}' \
        --adminpass='{{ moodle_new_adminpass | default('changeme') }}' \
        --adminemail='{{ moodle_new_instance_adminmail }}' \
        --agree-license
}

moodle_admin_password() {
    echo "Setting admin password..."
    php ${MOODLE_CLI_TOOLS}/reset-user-pass.php --userid=2 --hash="${1}"
}
{% if moodle_muc_config %}

moodle_muc_config() {
    echo "Applying MUC config"
    {{ moodle_muc_config_script }}
}
{% endif %}

moodle_instance_install() {
    database_check_with_retry 24 5

    install_check
    if [ $install_check_exit_code -eq 2 ]; then
        moodle_install
{% if moodle_new_adminpass_hash is defined %}
        moodle_admin_password '{{ moodle_new_adminpass_hash }}'
{% endif %}
{% if moodle_muc_config %}
        moodle_muc_config
{% endif %}
    elif [ $install_check_exit_code -eq 0 ]; then
        echo "WARNING: database already instantiated"
        exit 0
    else
        echo "Moodle could not be instantiated, exit code when checking database: '${install_check_exit_code}'"
        exit ${install_check_exit_code}
    fi
}

moodle_instance_update() {
    database_check_with_retry 10 1

    # get climaintenance to keep it in that state if preexisting
    climaintenance=$(test -f "{{ moodle_pvc_data_path }}/climaintenance.html" && echo true || echo false)
    echo "Upgrading moodle${MOODLE_UPDATE_MEMORY_LIMIT:+ with a memory limit of '${MOODLE_UPDATE_MEMORY_LIMIT}'}..."
    [ "${climaintenance}" != "true" ] && php ${MOODLE_APP}/admin/cli/maintenance.php --enable
    php ${MOODLE_UPDATE_MEMORY_LIMIT:+-d memory_limit=${MOODLE_UPDATE_MEMORY_LIMIT}} ${MOODLE_APP}/admin/cli/uninstall_plugins.php  --purge-missing --run
    php ${MOODLE_UPDATE_MEMORY_LIMIT:+-d memory_limit=${MOODLE_UPDATE_MEMORY_LIMIT}} ${MOODLE_APP}/admin/cli/upgrade.php --non-interactive
{% if moodle_muc_config %}
    moodle_muc_config
{% endif %}
    [ "${climaintenance}" != "true" ] && php ${MOODLE_APP}/admin/cli/maintenance.php --disable
}

moodle_cron() {
    database_check_with_retry 10 1

    echo "Running moodle cron..."
    MOODLE_CRON_MEMORY_LIMIT={{ moodle_cronjob_php_max_memory | default('') }}
    php ${MOODLE_CRON_MEMORY_LIMIT:+-d memory_limit=${MOODLE_CRON_MEMORY_LIMIT}} ${MOODLE_APP}/admin/cli/cron.php
}

while getopts ":iuc" opt; do
  case ${opt} in
    i )
        moodle_instance_install
        ;;
    u )
        moodle_instance_update
        ;;
    c )
        moodle_cron
        ;;
    \? )
        usage
        exit
        ;;
  esac
done
shift $((OPTIND -1))

if (( $OPTIND == 1 )); then
    echo -e "No check. Use an option:\n"
    usage
    exit
fi
  
```
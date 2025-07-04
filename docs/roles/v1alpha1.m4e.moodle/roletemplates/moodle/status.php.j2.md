



# status.php.j2

---
```

#!/usr/bin/php
<?php
define('CLI_SCRIPT', true);
define('NO_UPGRADE_CHECK', true);

$MOODLE_COMMIT = getenv('MOODLE_COMMIT') ?: false;
$MOODLE_APP = getenv('MOODLE_APP') ?: '/var/www/html';
require($MOODLE_APP . '/config.php');
require_once($CFG->libdir.'/clilib.php');

list($options, $unrecognized) = cli_get_params([
    'help'    => false,
    'checks' => false,
    'confighash' => false,
    'version' => false,
    'url' => false,
    'usage' => false
], [
    'h' => 'help',
    'c' => 'checks',
    'ch' => 'confighash',
    'v' => 'version',
    'l' => 'url',
    'u' => 'usage'
]);

if ($unrecognized) {
    $unrecognized = implode(PHP_EOL.'  ', $unrecognized);
    cli_error(get_string('cliunknowoption', 'core_admin', $unrecognized));
}

if ($options['help']) {
    cli_writeln("Get Moodle properties, usage and checks as json
Options:
    -h, --help                      Print out this help
    -c, --checks=critical,error     Include moodle checks
    -ch, --confighash              Include sha1 hash of config.php content
    -l, --url                       Include URL to access moodle
    -u, --usage                     Include moodle usage (storage and registered users)
    -v, --version                   Include moodle properties related with its version
Example:
\$ sudo -u www-data status.php -c -u -v");
    exit(2);
}

# array to export as json
$json = array();

# Convert bytes to gigabytes
function convertBytesToGiB($bytes) {
    return round($bytes / 1024 / 1024 / 1024,1);
}

if ($options['confighash']){
    $json['configHash'] = hash_file('sha1', $MOODLE_APP . '/config.php');
}

if ($options['url']){
    $json['url'] = "$CFG->wwwroot";
}

# will not run if upgrade running
if ($options['version'] && empty($CFG->upgraderunning)){
    # Source version to compare with db version later
    require("$CFG->dirroot/version.php");

    # Set update defaults
    $uptodate = "True";
    $version_source = $version;
    $version_source_release = $release;
    $version_source_branch = $branch;
    $version_source_pending_type = "None";
    $version_source_downgrade_error = "False";
    $version_source_allversionshash = $CFG->allversionshash;
    $version_source_pending = "False";

    # check if older version,
    # then check if empty values, and
    # finally check if inconsisten versions hash
    if ($version_source < $CFG->version) {
        $uptodate = "False";
        $version_source_downgrade_error = "True";
        $version_source_pending_type = "Other";
    } else if (empty($CFG->version) or empty($CFG->allversionshash)) {
        $uptodate = "False";
        $version_source_pending_type = "Other";
    } else {
        $version_source_allversionshash = core_component::get_all_versions_hash();
        if ($version_source_allversionshash !== $CFG->allversionshash){
            $uptodate = "False";
            $version_source_pending_type = "Other";
            if ($version_source > $CFG->version) {
                $version_source_pending_type = "Minor";
            }
            if ($branch !== $CFG->branch){
                $version_source_pending_type = "Major";
            }
        }
    }

    $json['upToDate'] = $uptodate;
    if ($uptodate !== "True") {
        $version_source_pending = "True";
        $json['state'] = "UpdatePending";
        $json['ready'] = "False";
    }
    $json['version'] = array(
        "allVersionsHash" => "$version_source_allversionshash",
        "branch" => "$version_source_branch",
        "downgradeError" => "$version_source_downgrade_error",
        "pending" => "$version_source_pending",
        "pendingType" => "$version_source_pending_type",
        "release" => "$version_source_release",
        "version" => "$version_source"
    );
}

if ($options['usage']){
    # get total files in bytes from moodle database
    $files_bytes_sql = "SELECT SUM(d.filesize) AS value
                        FROM (SELECT DISTINCT f.contenthash, f.filesize
                        FROM {files} f) d";
    $files_bytes = $DB->get_field_sql($files_bytes_sql);

    # get total database size in bytes
    $database_bytes_sql = "SELECT pg_database_size(?)";
    $database_bytes = $DB->get_field_sql($database_bytes_sql,[$CFG->dbname]);

    # get registered users (minus delete ones, guest and admin)
    $registered_users_sql = "SELECT COUNT(id) FROM {user} WHERE deleted = 0 AND id > 2";
    $registered_users = (int) $DB->get_field_sql($registered_users_sql);

    # save total storage of files in array
    $storage_files = array(
        "name" => "storage_files",
        "value" => convertBytesToGiB($files_bytes),
        "unit" => "GiB",
        "description" => "Total storage used for files"
    );

    # save total storage of database in array
    $storage_database = array(
        "name" => "storage_database",
        "value" => convertBytesToGiB($database_bytes),
        "unit" => "GiB",
        "description" => "Total storage used for database"
    );

    # save total storage in array
    $storage_total = array(
        "name" => 'storage_total',
        "value" => convertBytesToGiB($files_bytes+$database_bytes),
        "unit" => "GiB",
        "description" => "Total storage used (database + files)"
    );

    # save total users in array
    $users_total = array(
        "name" => "users_total",
        "value" => $registered_users,
        "unit" => "users",
        "description" => "Total users registered"
    );

    $json['usage'][] = $storage_files;
    $json['usage'][] = $storage_database;
    $json['usage'][] = $storage_total;
    $json['usage'][] = $users_total;
}

# will not run if upgrade running
if ($options['checks'] && empty($CFG->upgraderunning)){
    if (is_bool($options['checks'])){
        $filter_status = array('critical','error');
    }else{
        $filter_status = explode( ',', strtolower($options['checks']));
    }

    $types = array('status', 'security', 'performance');
    $all_checks = array();

    foreach ($types as $type){
        $method = 'get_' . $type . '_checks';
        $checks = \core\check\manager::$method();
        foreach ($checks as $check){
            $result = $check->get_result();
            $status = $result->get_status();
            if (empty($filter_status) || in_array("all", $filter_status) || in_array(strtolower($status), $filter_status)) {
                $type_check = array();
                // $action_link = $check->get_action_link();
                $type_check['type'] = $type;
                $type_check['status'] = $status;
                $type_check['ref'] = $check->get_ref();
                $type_check['name'] = $check->get_name();
                $type_check['summary'] = $result->get_summary();
                // $type_check['details'] = $result->get_details();
                // if ($actionlink){
                //     $type_check['actionLink']['name'] = $actionlink->name;
                //     $type_check['actionLink']['url'] = $actionlink->url;
                // }
                $all_checks[] = $type_check;
            }
        }
    }
    $json['checks'] = $all_checks;
}

# export as json
echo json_encode($json);
?>

```
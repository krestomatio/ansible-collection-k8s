



# php-fpm.yml

---
## moodle_php_fpm_database_check_socket

```

name: DATABASE_CHECK_SOCKET
value: '{{ moodle_config_dbhost }}:{{ moodle_config_dbport | default(''5432'') }}'

```
## moodle_php_fpm_envvar_data

```

name: MOODLE_DATA
value: '{{ moodle_pvc_data_path }}'

```
## moodle_php_fpm_envvar_data_readable

```

name: MOODLE_DATA_READABLE_DIR
value: '''{{ ''true'' if k8s_distribution == ''k8s'' else ''false'' }}'''

```
## moodle_php_fpm_envvar_config

```

name: MOODLE_CONFIG_DIR
value: '{{ moodle_config_path }}'

```
## moodle_php_fpm_envvar_redis

```

name: REDIS_PASSWORD
source: "secretKeyRef:\n  name: \"{{ moodle_redis_secret }}\"\n  key: \"{{ moodle_redis_secret_auth_key\
  \ }}\""

```
## moodle_php_fpm_envvars_base

```

'{{ [moodle_php_fpm_database_check_socket] + [moodle_php_fpm_envvar_data] + [moodle_php_fpm_envvar_data_readable]
  + [moodle_php_fpm_envvar_config] + ([moodle_php_fpm_envvar_redis] if moodle_redis_secret
  else []) }}'

```
## moodle_php_fpm_envvars_extra

```

[]

```
## moodle_php_fpm_volume_config

```

mount_path: '{{ moodle_config_path }}/config.php'
name: config-php
read_only: true
source: "secret:\n  secretName: \"{{ moodle_secret_config }}\"\n  items:\n  - key:\
  \ config.php\n    path: config.php\n  - key: \"{{ moodle_muc_config_json_file |\
  \ basename }}\"\n    path: \"{{ moodle_muc_config_json_file | basename }}\""
sub_path: config.php

```
## moodle_php_fpm_volume_muc_config

```

mount_path: '{{ moodle_muc_config_json_file }}'
name: config-php
read_only: true
sub_path: '{{ moodle_muc_config_json_file | basename }}'

```
## moodle_php_fpm_volume_localcache

```

mount_path: '{{ moodle_local_dir }}'
name: localcache
source: 'emptyDir: {}'

```
## moodle_php_fpm_volume_moodledata

```

'{{ moodle_volume_moodledata }}'

```
## moodle_php_fpm_volume_scripts

```

mount_path: '{{ moodle_scripts_path }}'
name: scripts
source: "configMap:\n  name: \"{{ moodle_cm_scripts }}\"\n  defaultMode: 0555"

```
## moodle_php_fpm_volumes_base

```

'{{ [moodle_php_fpm_volume_config] + [moodle_php_fpm_volume_muc_config] + [moodle_php_fpm_volume_moodledata]
  + [moodle_php_fpm_volume_localcache] + [moodle_php_fpm_volume_scripts] }}'

```
## moodle_php_fpm_volumes_extra

```

[]

```
## php_fpm_appname

```

'{{ meta_name }}-php-fpm'

```
## php_fpm_cm

```

'{{ php_fpm_appname }}-cm'

```
## php_fpm_inventory_uuid

```

'{{ (cr_group + cr_version + cr_kind + meta_namespace + meta_name) | to_uuid }}'

```
## php_fpm_image

```

'{{ moodle_image }}'

```
## php_fpm_image_pull_policy

```

'{{ moodle_image_pull_policy }}'

```
## php_fpm_container

```

moodle-php-fpm
...

```
## php_fpm_port

```

9000
...

```
## php_fpm_startup_probe

```

true
...

```
## php_fpm_startup_initial

```

0
...

```
## php_fpm_startup_period

```

10
...

```
## php_fpm_startup_failure

```

30
...

```
## php_fpm_startup_command

```

'{{ moodle_startup_command }}'

```
## php_fpm_readiness_probe

```

true
...

```
## php_fpm_readiness_command

```

'{{ moodle_readiness_command }}'

```
## php_fpm_liveness_probe

```

true
...

```
## php_fpm_liveness_command

```

'{{ moodle_liveness_command }}'

```
## php_fpm_connects_to

```

- '{{ moodle_postgres_appname }}'
- '{{ moodle_pgbouncer_appname }}'
- '{{ moodle_keydb_appname }}'
- '{{ moodle_nfs_appname }}'

```
## php_fpm_envvars

```

'{{ moodle_php_fpm_envvars_base + moodle_php_fpm_envvars_extra }}'

```
## php_fpm_volumes

```

'{{ moodle_php_fpm_volumes_base + moodle_php_fpm_volumes_extra }}'

```
## php_fpm_config_process_control_timeout

```

20
...

```
## php_fpm_netpol_omit

```

'{{ moodle_netpol_omit }}'

```
## php_fpm_netpol_ingress_ipblock

```

'{{ moodle_netpol_ingress_ipblock }}'

```
## php_fpm_netpol_egress_ipblock

```

'{{ moodle_netpol_egress_ipblock }}'

```
## php_fpm_netpol_ingress_extra_ports

```

'{{ moodle_netpol_ingress_extra_ports }}'

```
## php_fpm_netpol_egress_extra_ports

```

'{{ moodle_netpol_egress_extra_ports }}'

```
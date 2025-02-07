



# moodle.yml
  
---
## moodle_state
  
```

'{{ state }}'
  
```
## moodle_appname
  
```

'{{ meta_name }}-moodle'
  
```
## moodle_image
  
```

quay.io/krestomatio/moodle:4.1@sha256:77256c6f11a2113e2bd500cf4be548e069e408a16190a9383cb2040612f010b7
...
  
```
## moodle_image_pull_policy
  
```

IfNotPresent
...
  
```
## moodle_image_pull_secret
  
```

'{{ image_pull_secret }}'
  
```
## moodle_container
  
```

moodle-php-fpm
...
  
```
## moodle_container_group
  
```

'{{ moodle_container.replace(''-'', ''_'') }}'
  
```
## moodle_startup_command
  
```

'[''{{ moodle_php_fpm_check_container_script }}'', ''-s'']'
  
```
## moodle_readiness_command
  
```

'[''{{ moodle_php_fpm_check_container_script }}'', ''-r'']'
  
```
## moodle_liveness_command
  
```

'[''{{ moodle_php_fpm_check_container_script }}'', ''-l'']'
  
```
## moodle_php_fpm_check_container_script
  
```

/usr/libexec/check-container-php-moodle
...
  
```
## moodle_nginx_check_container_script
  
```

/usr/libexec/check-container-nginx-moodle
...
  
```
## moodle_service
  
```

'{{ moodle_appname }}-service'
  
```
## moodle_service_spec
  
```

"type: {{ moodle_service_type | default('ClusterIP') }}\nsessionAffinity: {{ moodle_service_session_affinity\
  \ | default('None') }}\n{% if moodle_service_session_affinity_timeout is defined\
  \ %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ moodle_service_session_affinity_timeout\
  \ }}\n{% endif %}\nports:\n- name: php-fpm\n  port: 9000\n  protocol: TCP\n  targetPort:\
  \ 9000\nselector:\n  app: '{{ moodle_appname }}'\n"
  
```
## moodle_app
  
```

/var/www/html
...
  
```
## moodle_config_path
  
```

/config
...
  
```
## moodle_scripts_path
  
```

'{{ moodle_config_path }}/scripts'
  
```
## moodle_local_dir
  
```

/var/moodlelocal
...
  
```
## moodle_host
  
```

m4e.krestomat.io
...
  
```
## moodle_port
  
```

false
...
  
```
## moodle_subpath
  
```

false
...
  
```
## moodle_protocol
  
```

http
...
  
```
## moodle_healthcheck_subpath
  
```

/login/index.php
...
  
```
## moodle_healthcheck_path
  
```

'{{ moodle_subpath | default('''',true) + moodle_healthcheck_subpath }}'
  
```
## moodle_config_autosync
  
```

true
...
  
```
## moodle_new_adminpass_hash
  
```

$2b$10$zbRuwPil1wNWQUkvlkchwe3/rOljJvoheydndKH1X0bdIIigy0xim
...
  
```
## moodle_new_instance
  
```

true
...
  
```
## moodle_new_instance_fullname
  
```

Demo site
...
  
```
## moodle_new_instance_shortname
  
```

demo
...
  
```
## moodle_new_instance_summary
  
```

A demo site
...
  
```
## moodle_new_instance_adminuser
  
```

admin
...
  
```
## moodle_new_instance_adminmail
  
```

admin@example.com
...
  
```
## moodle_new_instance_lang
  
```

en
...
  
```
## moodle_new_instance_agree_license
  
```

false
...
  
```
## moodle_new_instance_job
  
```

'{{ moodle_appname }}-new-instance-job'
  
```
## moodle_new_instance_job_ttl_seconds_after_finished
  
```

604800
...
  
```
## moodle_new_instance_job_active_deadline_seconds
  
```

3600
...
  
```
## moodle_new_instance_job_resource_requests
  
```

true
...
  
```
## moodle_new_instance_job_resource_requests_cpu
  
```

15m
...
  
```
## moodle_new_instance_job_resource_requests_memory
  
```

32Mi
...
  
```
## moodle_new_instance_job_resource_limits
  
```

false
...
  
```
## moodle_new_instance_job_resource_limits_cpu
  
```

1
...
  
```
## moodle_new_instance_job_resource_limits_memory
  
```

1Gi
...
  
```
## moodle_new_instance_job_php_fpm_config_process_control_timeout
  
```

'{{ php_fpm_config_process_control_timeout }}'
  
```
## moodle_new_instance_job_command
  
```

- /bin/bash
- -c
- 'container-entrypoint

  {{ moodle_scripts_path }}/moodle-instance -i

  {% if moodle_new_instance_job_command_snippet | default(false) %}

  {{ moodle_new_instance_job_command_snippet }}

  {% endif %}

  '
  
```
## moodle_new_instance_job_php_max_memory
  
```

'{{ moodle_new_instance_job_resource_limits_memory | regex_search(''^\d+[MmGgKk]'')
  if moodle_new_instance_job_resource_limits_memory is defined and moodle_new_instance_job_resource_limits
  else '''' }}'
  
```
## moodle_new_instance_job_tolerations
  
```

false
...
  
```
## moodle_new_instance_job_node_selector
  
```

false
...
  
```
## moodle_new_instance_job_affinity
  
```

false
...
  
```
## moodle_new_instance_job_php_fpm_database_check_socket
  
```

'{{ moodle_php_fpm_database_check_socket }}'
  
```
## moodle_new_instance_job_startup_probe
  
```

true
...
  
```
## moodle_new_instance_job_startup_command
  
```

'[''{{ moodle_php_fpm_check_container_script }}'', ''-d'']'
  
```
## moodle_new_instance_job_startup_initial
  
```

0
...
  
```
## moodle_new_instance_job_startup_period
  
```

10
...
  
```
## moodle_new_instance_job_startup_timeout
  
```

3
...
  
```
## moodle_new_instance_job_startup_success
  
```

1
...
  
```
## moodle_new_instance_job_startup_failure
  
```

12
...
  
```
## moodle_new_instance_job_connects_to
  
```

'{{ php_fpm_connects_to }}'
  
```
## moodle_update_allow_pending_types
  
```

- Other
- Minor
  
```
## moodle_update_job
  
```

'{{ moodle_appname }}-update-{{ moodle_status_version.allVersionsHash[:10] | default(now(utc=True).timestamp()
  | int) }}-job'
  
```
## moodle_update_job_ttl_seconds_after_finished
  
```

604800
...
  
```
## moodle_update_job_active_deadline_seconds
  
```

'{{ 21600 if moodle_status_version.pendingType | default(''Other'') == ''Major'' else
  10800 }}'
  
```
## moodle_update_job_resource_requests
  
```

true
...
  
```
## moodle_update_job_resource_requests_cpu
  
```

15m
...
  
```
## moodle_update_job_resource_requests_memory
  
```

32Mi
...
  
```
## moodle_update_job_resource_limits
  
```

false
...
  
```
## moodle_update_job_resource_limits_cpu
  
```

1
...
  
```
## moodle_update_job_resource_limits_memory
  
```

1Gi
...
  
```
## moodle_update_job_command
  
```

- /bin/bash
- -c
- 'container-entrypoint

  {{ moodle_scripts_path }}/moodle-instance -u

  {% if moodle_update_job_command_snippet | default(false) %}

  {{ moodle_update_job_command_snippet }}

  {% endif %}

  '
  
```
## moodle_update_job_php_max_memory
  
```

'{{ moodle_update_job_resource_limits_memory | regex_search(''^\d+[MmGgKk]'') if moodle_update_job_resource_limits_memory
  is defined and moodle_update_job_resource_limits else '''' }}'
  
```
## moodle_update_job_php_fpm_config_process_control_timeout
  
```

'{{ php_fpm_config_process_control_timeout }}'
  
```
## moodle_update_job_tolerations
  
```

false
...
  
```
## moodle_update_job_node_selector
  
```

false
...
  
```
## moodle_update_job_affinity
  
```

false
...
  
```
## moodle_update_job_php_fpm_database_check_socket
  
```

'{{ moodle_php_fpm_database_check_socket }}'
  
```
## moodle_update_job_connects_to
  
```

'{{ php_fpm_connects_to }}'
  
```
## moodle_cronjob
  
```

'{{ moodle_appname }}-cronjob'
  
```
## moodle_cronjob_schedule
  
```

'*/1 * * * *'
  
```
## moodle_cronjob_success_limit
  
```

3
...
  
```
## moodle_cronjob_starting_deadline_seconds
  
```

45
...
  
```
## moodle_cronjob_failed_limit
  
```

1
...
  
```
## moodle_cronjob_completions
  
```

1
...
  
```
## moodle_cronjob_parallelism
  
```

1
...
  
```
## moodle_cronjob_backoff_limit
  
```

1
...
  
```
## moodle_cronjob_active_deadline_seconds
  
```

86400
...
  
```
## moodle_cronjob_suspend
  
```

false
...
  
```
## moodle_cronjob_concurrency_policy
  
```

Allow
...
  
```
## moodle_cronjob_command
  
```

- /bin/bash
- -c
- 'container-entrypoint

  {{ moodle_scripts_path }}/moodle-instance -c

  {% if moodle_cronjob_command_snippet | default(false) %}

  {{ moodle_cronjob_command_snippet }}

  {% endif %}

  '
  
```
## moodle_cronjob_php_max_memory
  
```

'{{ moodle_cronjob_resource_limits_memory | regex_search(''^\d+[MmGgKk]'') if moodle_cronjob_resource_limits_memory
  is defined and moodle_cronjob_resource_limits else '''' }}'
  
```
## moodle_cronjob_resource_requests
  
```

true
...
  
```
## moodle_cronjob_resource_requests_cpu
  
```

15m
...
  
```
## moodle_cronjob_resource_requests_memory
  
```

32Mi
...
  
```
## moodle_cronjob_resource_limits
  
```

false
...
  
```
## moodle_cronjob_resource_limits_cpu
  
```

1
...
  
```
## moodle_cronjob_resource_limits_memory
  
```

1Gi
...
  
```
## moodle_cronjob_php_fpm_config_process_control_timeout
  
```

'{{ php_fpm_config_process_control_timeout }}'
  
```
## moodle_cronjob_tolerations
  
```

false
...
  
```
## moodle_cronjob_node_selector
  
```

false
...
  
```
## moodle_cronjob_affinity
  
```

false
...
  
```
## moodle_cronjob_connects_to
  
```

'{{ php_fpm_connects_to }}'
  
```
## moodle_cronjob_vpa
  
```

'{{ moodle_cronjob }}-vpa'
  
```
## moodle_cronjob_vpa_spec
  
```

false
...
  
```
## moodle_cronjob_php_fpm_database_check_socket
  
```

'{{ moodle_php_fpm_database_check_socket }}'
  
```
## moodle_cronjob_ttl_seconds_after_finished
  
```

604800
...
  
```
## moodle_pvc_data
  
```

'{{ moodle_appname }}-moodledata-pvc'
  
```
## moodle_pvc_data_storage_access_mode
  
```

ReadWriteOnce
...
  
```
## moodle_pvc_data_storage_class_name
  
```

false
...
  
```
## moodle_pvc_data_path
  
```

/var/moodledata
...
  
```
## moodle_pvc_data_spec
  
```

"{% if moodle_pvc_data_storage_class_name is defined and moodle_pvc_data_storage_class_name\
  \ %}\nstorageClassName: {{ moodle_pvc_data_storage_class_name }}\n{% endif %}\n\
  accessModes:\n  - '{{ moodle_pvc_data_storage_access_mode }}'\nresources:\n  requests:\n\
  \    storage: '{{ moodle_pvc_data_size }}'\n"
  
```
## moodle_pvc_data_source
  
```

"persistentVolumeClaim:\n  claimName: \"{{ moodle_pvc_data }}\""
  
```
## moodle_pvc_data_current_size
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''PersistentVolumeClaim'', namespace=meta_namespace,resource_name=moodle_pvc_data).spec.resources.requests.storage
  | default('''') }}'
  
```
## moodle_pvc_data_size
  
```

'{{ moodle_pvc_data_size_gib | string + ''Gi'' if moodle_pvc_data_autoexpansion else
  moodle_pvc_data_current_size | default(''1Gi'', true) }}'
  
```
## moodle_pvc_data_size_gib
  
```

'{{ cr_status_properties[routine_pvc_autoexpand_info_keyname].autoexpandSizeGib |
  default(moodle_pvc_data_autoexpansion_increment_gib) }}'
  
```
## moodle_pvc_data_autoexpansion
  
```

false
...
  
```
## moodle_pvc_data_autoexpansion_increment_gib
  
```

1
...
  
```
## moodle_pvc_data_autoexpansion_cap_gib
  
```

5
...
  
```
## moodle_netpol_omit
  
```

true
...
  
```
## moodle_nfs_meta_name
  
```

false
...
  
```
## moodle_nfs_appname
  
```

'{{ moodle_nfs_meta_name + ''-nfs'' if moodle_nfs_meta_name else false }}'
  
```
## moodle_nfs_service
  
```

'{{ moodle_nfs_meta_name + ''-nfs-service'' if moodle_nfs_meta_name else '''' }}'
  
```
## moodle_nfs_namespace
  
```

'{{ meta_namespace }}'
  
```
## moodle_nfs_parent_domain
  
```

false
...
  
```
## moodle_nfs_domain
  
```

'{{ moodle_nfs_namespace + ( ''.'' + moodle_nfs_parent_domain if moodle_nfs_parent_domain
  else '''') }}'
  
```
## moodle_nfs_data_server
  
```

'{{ moodle_nfs_service + ''.'' + moodle_nfs_domain if moodle_nfs_meta_name else ''''
  }}'
  
```
## moodle_nfs_data_share
  
```

/
...
  
```
## moodle_nfs_data_source
  
```

"csi:\n  driver: nfs.csi.k8s.io\n  volumeAttributes:\n    server: \"{{ moodle_nfs_data_server\
  \ }}\"  # required\n    share: \"{{ moodle_nfs_data_share }}\"  # required\n{% if\
  \ moodle_nfs_data_mount_options is defined and moodle_nfs_data_mount_options %}\n\
  \    mountOptions: \"{{ moodle_nfs_data_mount_options }}\"  # optional\n{% endif\
  \ %}\n{% if moodle_nfs_data_mount_permissions is defined and moodle_nfs_data_mount_permissions\
  \ %}\n    mountPermissions: \"{{ moodle_nfs_data_mount_permissions }}\"  # optional\n\
  {% endif %}"
  
```
## moodle_volume_moodledata
  
```

mount_path: '{{ moodle_pvc_data_path }}'
name: moodledata
source: '{{ moodle_nfs_data_source if moodle_nfs_meta_name else moodle_pvc_data_source
  }}'
  
```
## moodle_secret_config
  
```

'{{ moodle_appname }}-secret-config'
  
```
## moodle_secret_config_data
  
```

'config.php: ''{{ lookup(''template'', moodle_config_template) | b64encode }}''

  muc-config.json: ''{{ lookup(''template'', moodle_muc_config_template) | to_json
  | b64encode }}''

  '
  
```
## moodle_secret_admin
  
```

'{{ moodle_appname }}-secret-admin'
  
```
## moodle_secret_admin_data
  
```

'password_hash: ''{{ moodle_new_adminpass_hash | b64encode }}''

  '
  
```
## moodle_cm_scripts
  
```

'{{ moodle_appname }}-cm-scripts'
  
```
## moodle_cm_scripts_data
  
```

"muc-config.php: |\n  {{ lookup('template', moodle_script_muc_config_template) | indent(2)\
  \ }}\nstatus.php: |\n  {{ lookup('template', moodle_script_status_template) | indent(2)\
  \ }}\nmoodle-instance: |\n  {{ lookup('template', moodle_instance_template) | indent(2)\
  \ }}\n"
  
```
## moodle_postgres_meta_name
  
```

false
...
  
```
## moodle_postgres_appname
  
```

'{{ moodle_postgres_meta_name + ''-postgres'' if moodle_postgres_meta_name else false
  }}'
  
```
## moodle_pgbouncer_meta_name
  
```

'{{ moodle_postgres_meta_name if moodle_postgres_meta_name else false }}'
  
```
## moodle_pgbouncer_appname
  
```

'{{ moodle_pgbouncer_meta_name + ''-pgbouncer'' if moodle_pgbouncer_meta_name else
  false }}'
  
```
## moodle_database_service
  
```

'{{ moodle_pgbouncer_appname + ''-service'' if moodle_pgbouncer_meta_name else ''''
  }}'
  
```
## moodle_database_secret
  
```

'{{ moodle_postgres_appname + ''-secret'' if moodle_postgres_meta_name else '''' }}'
  
```
## moodle_database_secret_dbname_key
  
```

database_name
...
  
```
## moodle_database_secret_dbuser_key
  
```

database_user
...
  
```
## moodle_database_secret_dbpass_key
  
```

database_password
...
  
```
## moodle_keydb_meta_name
  
```

false
...
  
```
## moodle_keydb_appname
  
```

'{{ moodle_keydb_meta_name + ''-keydb'' if moodle_keydb_meta_name else false }}'
  
```
## moodle_redis_service
  
```

'{{ moodle_keydb_meta_name + ''-keydb-service'' if moodle_keydb_meta_name else ''''
  }}'
  
```
## moodle_redis_secret
  
```

'{{ moodle_keydb_meta_name + ''-keydb-secret'' if moodle_keydb_meta_name else ''''
  }}'
  
```
## moodle_redis_secret_auth_key
  
```

keydb_password
...
  
```
## moodle_redis_host
  
```

'{{ moodle_redis_service }}'
  
```
## moodle_redis_session_store
  
```

'{{ true if moodle_keydb_meta_name else false }}'
  
```
## moodle_redis_password
  
```

'{{ '''' if not moodle_redis_secret else lookup(''k8s'', api_version=''v1'', kind=''Secret'',
  namespace=meta_namespace, resource_name=moodle_redis_secret).data [moodle_redis_secret_auth_key
  | default(''redis_password'')] | default('''') | b64decode }}'
  
```
## moodle_redis_muc_config
  
```

'{{ true if moodle_keydb_meta_name else false }}'
  
```
## moodle_redis_muc_config_prefix
  
```

muc_
...
  
```
## moodle_redis_muc_config_serializer
  
```

2
...
  
```
## moodle_redis_muc_config_compressor
  
```

1
...
  
```
## moodle_muc_config
  
```

'{{ moodle_redis_muc_config }}'
  
```
## moodle_muc_config_script
  
```

php -d apc.enable_cli=1 {{ moodle_scripts_path }}/muc-config.php {% if moodle_muc_config_reset
  %} -r {% endif %} -f='{{moodle_muc_config_json_file }}'
...
  
```
## moodle_muc_config_reset
  
```

false
...
  
```
## moodle_muc_config_json_file
  
```

'{{ moodle_config_path }}/muc-config.json'
  
```
## moodle_config_dbhost
  
```

'{{ moodle_database_service }}'
  
```
## moodle_config_dbname
  
```

'{{ '''' if not moodle_database_secret else lookup(''k8s'', api_version=''v1'', kind=''Secret'',
  namespace=meta_namespace, resource_name=moodle_database_secret).data[moodle_database_secret_dbname_key]
  | default('''') | b64decode }}'
  
```
## moodle_config_dbuser
  
```

'{{ '''' if not moodle_database_secret else lookup(''k8s'', api_version=''v1'', kind=''Secret'',
  namespace=meta_namespace, resource_name=moodle_database_secret).data[moodle_database_secret_dbuser_key]
  | default('''') | b64decode }}'
  
```
## moodle_config_dbpass
  
```

'{{ '''' if not moodle_database_secret else lookup(''k8s'', api_version=''v1'', kind=''Secret'',
  namespace=meta_namespace, resource_name=moodle_database_secret).data[moodle_database_secret_dbpass_key]
  | default('''') | b64decode }}'
  
```
## moodle_config_wwwroot
  
```

'{{ moodle_protocol }}://{{ moodle_host + ( '':'' + moodle_port | string if moodle_port
  else '''' ) + ( moodle_subpath if moodle_subpath else '''' ) }}'
  
```
## moodle_config_dataroot
  
```

'{{ moodle_pvc_data_path }}'
  
```
## moodle_config_dbhandlesoptions
  
```

'{{ moodle_database_service is search(''pgbouncer'') if moodle_postgres_meta_name
  else false }}'
  
```
## moodle_config_session_redis
  
```

'{{ moodle_redis_session_store }}'
  
```
## moodle_config_session_redis_host
  
```

'{{ moodle_redis_host }}'
  
```
## moodle_config_session_redis_auth
  
```

'{{ moodle_redis_password }}'
  
```
## moodle_config_session_redis_acquire_lock_timeout
  
```

120
...
  
```
## moodle_config_session_redis_lock_expire
  
```

7200
...
  
```
## moodle_config_sslproxy
  
```

'{{ true if moodle_protocol == ''https'' else false }}'
  
```
## moodle_config_localcachedir
  
```

'{{ moodle_local_dir }}/cache'
  
```
## moodle_config_disableupdateautodeploy
  
```

true
...
  
```
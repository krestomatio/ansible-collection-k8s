



# nginx.yml
  
---
## moodle_nginx_envvar_fastcgi_pass
  
```

name: NGINX_FASTCGI_PASS
value: '{{ php_fpm_appname }}-service:{{ php_fpm_port }}'
  
```
## moodle_nginx_envvar_moodle_check_host
  
```

name: MOODLE_CHECK_HOST
value: '{{ moodle_host + ( '':'' + moodle_port | string if moodle_port else '''' )
  }}'
  
```
## moodle_nginx_envvar_moodle_check_path
  
```

name: MOODLE_CHECK_PATH
value: '{{ moodle_healthcheck_path }}'
  
```
## moodle_nginx_envvars_base
  
```

'{{ [moodle_nginx_envvar_fastcgi_pass] + [moodle_nginx_envvar_moodle_check_host] +
  [moodle_nginx_envvar_moodle_check_path] }}'
  
```
## moodle_nginx_envvars_extra
  
```

[]
  
```
## moodle_nginx_volume_moodledata
  
```

'{{ moodle_volume_moodledata }}'
  
```
## moodle_nginx_volumes_base
  
```

'{{ [moodle_nginx_volume_moodledata] }}'
  
```
## moodle_nginx_volumes_extra
  
```

[]
  
```
## nginx_appname
  
```

'{{ meta_name }}-nginx'
  
```
## nginx_inventory_uuid
  
```

'{{ (cr_group + cr_version + cr_kind + meta_namespace + meta_name) | to_uuid }}'
  
```
## nginx_image
  
```

'{{ moodle_image }}'
  
```
## nginx_image_pull_policy
  
```

'{{ moodle_image_pull_policy }}'
  
```
## nginx_container
  
```

moodle-nginx
...
  
```
## nginx_startup_probe
  
```

true
...
  
```
## nginx_startup_initial
  
```

0
...
  
```
## nginx_startup_command
  
```

'[''{{ moodle_nginx_check_container_script }}'', ''-s'']'
  
```
## nginx_readiness_probe
  
```

true
...
  
```
## nginx_readiness_command
  
```

'[''{{ moodle_nginx_check_container_script }}'', ''-r'']'
  
```
## nginx_liveness_probe
  
```

true
...
  
```
## nginx_liveness_command
  
```

'[''{{ moodle_nginx_check_container_script }}'', ''-l'']'
  
```
## nginx_connects_to
  
```

'{{ php_fpm_appname | default(moodle_appname + ''-php-fpm'') }}'
  
```
## nginx_ingress_host
  
```

'{{ moodle_host }}'
  
```
## nginx_ingress_protocol
  
```

'{{ moodle_protocol }}'
  
```
## nginx_envvars
  
```

'{{ moodle_nginx_envvars_base + moodle_nginx_envvars_extra }}'
  
```
## nginx_volumes
  
```

'{{ moodle_nginx_volumes_base + moodle_nginx_volumes_extra }}'
  
```
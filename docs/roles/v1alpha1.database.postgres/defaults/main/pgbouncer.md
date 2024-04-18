



# pgbouncer.yml
  
---
## pgbouncer_state
  
```

'{{ state }}'
  
```
## pgbouncer_appname
  
```

'{{ meta_name }}-pgbouncer'
  
```
## pgbouncer_readonly_appname
  
```

'{{ meta_name }}-pgbouncer-readonly'
  
```
## pgbouncer_image
  
```

quay.io/krestomatio/pgbouncer@sha256:fc401e5f51e88a014d8250cabc82dd4cd40c95d920a26feebc1ded78f6f00ee0
...
  
```
## pgbouncer_image_pull_secret
  
```

'{{ image_pull_secret }}'
  
```
## pgbouncer_deploy
  
```

'{{ pgbouncer_appname }}-deploy'
  
```
## pgbouncer_container
  
```

pgbouncer
...
  
```
## pgbouncer_container_group
  
```

'{{ pgbouncer_container.replace(''-'', ''_'') }}'
  
```
## pgbouncer_startup_probe
  
```

true
...
  
```
## pgbouncer_startup_command
  
```

'[''/usr/libexec/check-container-pgbouncer'', ''-r'']'
  
```
## pgbouncer_startup_initial
  
```

5
...
  
```
## pgbouncer_startup_period
  
```

10
...
  
```
## pgbouncer_startup_timeout
  
```

1
...
  
```
## pgbouncer_startup_success
  
```

1
...
  
```
## pgbouncer_startup_failure
  
```

3
...
  
```
## pgbouncer_readiness_probe
  
```

true
...
  
```
## pgbouncer_readiness_command
  
```

'[''/usr/libexec/check-container-pgbouncer'']'
  
```
## pgbouncer_readiness_initial
  
```

5
...
  
```
## pgbouncer_readiness_period
  
```

10
...
  
```
## pgbouncer_readiness_timeout
  
```

1
...
  
```
## pgbouncer_readiness_success
  
```

1
...
  
```
## pgbouncer_readiness_failure
  
```

3
...
  
```
## pgbouncer_liveness_probe
  
```

true
...
  
```
## pgbouncer_liveness_command
  
```

'[''/usr/libexec/check-container-pgbouncer'', ''--live'']'
  
```
## pgbouncer_liveness_initial
  
```

120
...
  
```
## pgbouncer_liveness_period
  
```

10
...
  
```
## pgbouncer_liveness_timeout
  
```

10
...
  
```
## pgbouncer_liveness_success
  
```

1
...
  
```
## pgbouncer_liveness_failure
  
```

3
...
  
```
## pgbouncer_resource_requests
  
```

true
...
  
```
## pgbouncer_resource_requests_cpu
  
```

15m
...
  
```
## pgbouncer_resource_requests_memory
  
```

32Mi
...
  
```
## pgbouncer_resource_limits
  
```

false
...
  
```
## pgbouncer_resource_limits_cpu
  
```

1
...
  
```
## pgbouncer_resource_limits_memory
  
```

1Gi
...
  
```
## pgbouncer_term_grace_period
  
```

30
...
  
```
## pgbouncer_tolerations
  
```

false
...
  
```
## pgbouncer_node_selector
  
```

false
...
  
```
## pgbouncer_affinity
  
```

false
...
  
```
## pgbouncer_port
  
```

5432
...
  
```
## pgbouncer_readonly_deploy
  
```

'{{ pgbouncer_readonly_appname }}-deploy'
  
```
## pgbouncer_readonly_container
  
```

postgres-readreplica
...
  
```
## pgbouncer_readonly_container_group
  
```

'{{ pgbouncer_readonly_container.replace(''-'', ''_'') }}'
  
```
## pgbouncer_readonly_startup_probe
  
```

'{{ pgbouncer_startup_probe }}'
  
```
## pgbouncer_readonly_startup_command
  
```

'{{ pgbouncer_startup_command }}'
  
```
## pgbouncer_readonly_startup_initial
  
```

'{{ pgbouncer_startup_initial }}'
  
```
## pgbouncer_readonly_startup_period
  
```

'{{ pgbouncer_startup_period }}'
  
```
## pgbouncer_readonly_startup_timeout
  
```

'{{ pgbouncer_startup_timeout }}'
  
```
## pgbouncer_readonly_startup_success
  
```

'{{ pgbouncer_startup_success }}'
  
```
## pgbouncer_readonly_startup_failure
  
```

'{{ pgbouncer_startup_failure }}'
  
```
## pgbouncer_readonly_readiness_probe
  
```

'{{ pgbouncer_readiness_probe }}'
  
```
## pgbouncer_readonly_readiness_command
  
```

'{{ pgbouncer_readiness_command }}'
  
```
## pgbouncer_readonly_readiness_initial
  
```

'{{ pgbouncer_readiness_initial }}'
  
```
## pgbouncer_readonly_readiness_period
  
```

'{{ pgbouncer_readiness_period }}'
  
```
## pgbouncer_readonly_readiness_timeout
  
```

'{{ pgbouncer_readiness_timeout }}'
  
```
## pgbouncer_readonly_readiness_success
  
```

'{{ pgbouncer_readiness_success }}'
  
```
## pgbouncer_readonly_readiness_failure
  
```

'{{ pgbouncer_readiness_failure }}'
  
```
## pgbouncer_readonly_liveness_probe
  
```

'{{ pgbouncer_liveness_probe }}'
  
```
## pgbouncer_readonly_liveness_command
  
```

'{{ pgbouncer_liveness_command }}'
  
```
## pgbouncer_readonly_liveness_initial
  
```

'{{ pgbouncer_liveness_initial }}'
  
```
## pgbouncer_readonly_liveness_period
  
```

'{{ pgbouncer_liveness_period }}'
  
```
## pgbouncer_readonly_liveness_timeout
  
```

'{{ pgbouncer_liveness_timeout }}'
  
```
## pgbouncer_readonly_liveness_success
  
```

'{{ pgbouncer_liveness_success }}'
  
```
## pgbouncer_readonly_liveness_failure
  
```

'{{ pgbouncer_liveness_failure }}'
  
```
## pgbouncer_readonly_resource_requests
  
```

'{{ pgbouncer_resource_requests }}'
  
```
## pgbouncer_readonly_resource_requests_cpu
  
```

'{{ pgbouncer_resource_requests_cpu }}'
  
```
## pgbouncer_readonly_resource_requests_memory
  
```

'{{ pgbouncer_resource_requests_memory }}'
  
```
## pgbouncer_readonly_resource_limits
  
```

'{{ pgbouncer_resource_limits }}'
  
```
## pgbouncer_readonly_resource_limits_cpu
  
```

'{{ pgbouncer_resource_limits_cpu }}'
  
```
## pgbouncer_readonly_resource_limits_memory
  
```

'{{ pgbouncer_resource_limits_memory }}'
  
```
## pgbouncer_readonly_term_grace_period
  
```

'{{ pgbouncer_term_grace_period }}'
  
```
## pgbouncer_readonly_tolerations
  
```

'{{ pgbouncer_tolerations }}'
  
```
## pgbouncer_readonly_node_selector
  
```

'{{ pgbouncer_node_selector }}'
  
```
## pgbouncer_readonly_affinity
  
```

'{{ pgbouncer_affinity }}'
  
```
## pgbouncer_secret
  
```

'{{ pgbouncer_appname }}-secret'
  
```
## pgbouncer_admin_database
  
```

'{{ lookup(''password'', ''/dev/null chars=ascii_lowercase length=8'') }}'
  
```
## pgbouncer_admin_user
  
```

'{{ lookup(''password'', ''/dev/null chars=ascii_lowercase length=8'') }}'
  
```
## pgbouncer_admin_password
  
```

'{{ lookup(''password'', ''/dev/null'') }}'
  
```
## pgbouncer_secret_data
  
```

"pgbouncer_admin_database: {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=pgbouncer_secret).data.pgbouncer_admin_database |\n  default(pgbouncer_admin_database\
  \ |\n  b64encode,true) }}\npgbouncer_admin_user: {{ lookup('k8s', api_version='v1',\
  \ kind='Secret', namespace=meta_namespace,\n  resource_name=pgbouncer_secret).data.pgbouncer_admin_user\
  \ |\n  default(pgbouncer_admin_user |\n  b64encode,true) }}\npgbouncer_admin_password:\
  \ {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=pgbouncer_secret).data.pgbouncer_admin_password |\n  default(pgbouncer_admin_password\
  \ |\n  b64encode,true) }}\npgbouncer_database_url: {{ lookup('k8s', api_version='v1',\
  \ kind='Secret', namespace=meta_namespace,\n  resource_name=pgbouncer_secret).data.pgbouncer_database_url\
  \ |\n  default(('postgres://' + lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=postgres_secret).data.database_user | default(postgres_database_user)\n\
  \  + ':' + lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=postgres_secret).data.database_password | default(postgres_database_password)\n\
  \  + '@' + pgbouncer_service + ':' + pgbouncer_port | string + '/'\n  + lookup('k8s',\
  \ api_version='v1', kind='Secret', namespace=meta_namespace,\n  resource_name=postgres_secret).data.database_password\
  \ | default(postgres_database_name)) |\n  b64encode,true) }}\n"
  
```
## pgbouncer_readonly_secret
  
```

'{{ pgbouncer_readonly_appname }}-secret'
  
```
## pgbouncer_readonly_admin_database
  
```

'{{ lookup(''password'', ''/dev/null chars=ascii_lowercase length=8'') }}'
  
```
## pgbouncer_readonly_admin_user
  
```

'{{ lookup(''password'', ''/dev/null chars=ascii_lowercase length=8'') }}'
  
```
## pgbouncer_readonly_admin_password
  
```

'{{ lookup(''password'', ''/dev/null'') }}'
  
```
## pgbouncer_readonly_secret_data
  
```

"pgbouncer_readonly_admin_database: {{ lookup('k8s', api_version='v1', kind='Secret',\
  \ namespace=meta_namespace,\n  resource_name=pgbouncer_readonly_secret).data.pgbouncer_readonly_admin_database\
  \ |\n  default(pgbouncer_readonly_admin_database |\n  b64encode,true) }}\npgbouncer_readonly_admin_user:\
  \ {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=pgbouncer_readonly_secret).data.pgbouncer_readonly_admin_user |\n\
  \  default(pgbouncer_readonly_admin_user |\n  b64encode,true) }}\npgbouncer_readonly_admin_password:\
  \ {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=pgbouncer_readonly_secret).data.pgbouncer_readonly_admin_password\
  \ |\n  default(pgbouncer_readonly_admin_password |\n  b64encode,true) }}\npgbouncer_readonly_database_url:\
  \ {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=pgbouncer_readonly_secret).data.pgbouncer_readonly_database_url\
  \ |\n  default(('postgres://' + lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=postgres_secret).data.database_user | default(postgres_database_user)\n\
  \  + ':' + lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=postgres_secret).data.database_password | default(postgres_database_password)\n\
  \  + '@' + pgbouncer_readonly_service + ':' + pgbouncer_port | string + '/'\n  +\
  \ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n  resource_name=postgres_secret).data.database_password\
  \ | default(postgres_database_name)) |\n  b64encode,true) }}\n"
  
```
## pgbouncer_service
  
```

'{{ pgbouncer_appname }}-service'
  
```
## pgbouncer_service_spec
  
```

"type: {{ pgbouncer_service_type | default('ClusterIP') }}\nselector:\n  app: '{{\
  \ pgbouncer_appname }}'\nports:\n  - name: pgbouncer\n    port: {{ pgbouncer_port\
  \ }}\n    protocol: TCP\n    targetPort: {{ pgbouncer_port }}\nsessionAffinity:\
  \ {{ pgbouncer_service_session_affinity | default('None') }}\n{% if pgbouncer_service_session_affinity_timeout\
  \ is defined %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ pgbouncer_service_session_affinity_timeout\
  \ }}\n{% endif %}\n"
  
```
## pgbouncer_readonly_service
  
```

'{{ pgbouncer_readonly_appname }}-service'
  
```
## pgbouncer_readonly_service_spec
  
```

"type: {{ pgbouncer_service_type | default('ClusterIP') }}\nselector:\n  app: '{{\
  \ pgbouncer_readonly_appname }}'\nports:\n  - name: pgbouncer\n    port: {{ pgbouncer_port\
  \ }}\n    protocol: TCP\n    targetPort: {{ pgbouncer_port }}\nsessionAffinity:\
  \ {{ pgbouncer_readonly_service_session_affinity | default('None') }}\n{% if pgbouncer_readonly_service_session_affinity_timeout\
  \ is defined %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ pgbouncer_readonly_service_session_affinity_timeout\
  \ }}\n{% endif %}\n"
  
```
## pgbouncer_cm
  
```

'{{ pgbouncer_appname }}-cm'
  
```
## pgbouncer_cm_data
  
```

"pgbouncer-extra.ini: |\n  {{ pgbouncer_extra_config | default('') | indent(2) }}\n\
  pgbouncer-extra-users.ini: |\n  {{ pgbouncer_extra_users_config | default('') |\
  \ indent(2) }}\npgbouncer-extra-databases.ini: |\n  {{ pgbouncer_extra_databases_config\
  \ | default('') | indent(2) }}\n"
  
```
## pgbouncer_readonly_cm
  
```

'{{ pgbouncer_readonly_appname }}-cm'
  
```
## pgbouncer_readonly_cm_data
  
```

"pgbouncer-extra.ini: |\n  ;; https://www.pgbouncer.org/faq.html#how-to-load-balance-queries-between-several-servers\n\
  \  server_lifetime = {{ pgbouncer_readonly_server_lifetime | default('1200') }}\n\
  \  server_round_robin = {{ pgbouncer_readonly_server_round_robin | default('1')\
  \ }}\n  {{ pgbouncer_readonly_extra_config | default(pgbouncer_extra_config) | default('')\
  \ | indent(2) }}\npgbouncer-extra-users.ini: |\n  {{ pgbouncer_readonly_extra_users_config\
  \ | default(pgbouncer_extra_users_config) | default('') | indent(2) }}\npgbouncer-extra-databases.ini:\
  \ |\n  {{ pgbouncer_readonly_extra_databases_config | default(pgbouncer_extra_databases_config)\n\
  \  | default('') | indent(2) }}\n"
  
```
## pgbouncer_vpa
  
```

'{{ pgbouncer_appname }}-vpa'
  
```
## pgbouncer_vpa_spec
  
```

false
...
  
```
## pgbouncer_readonly_vpa
  
```

'{{ pgbouncer_readonly_appname }}-vpa'
  
```
## pgbouncer_readonly_vpa_spec
  
```

false
...
  
```
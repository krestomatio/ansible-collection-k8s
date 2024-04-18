



# postgres.yml
  
---
## postgres_state
  
```

'{{ state }}'
  
```
## postgres_appname
  
```

'{{ meta_name }}-postgres'
  
```
## postgres_mode
  
```

standalone
...
  
```
## postgres_readreplicas_appname
  
```

'{{ meta_name }}-readreplicas'
  
```
## postgres_image
  
```

quay.io/krestomatio/postgres:13@sha256:e3e6cee638483466e76ae65bb75d47e6b627a5261033630440c8da987e1d16f4
...
  
```
## postgres_image_pull_secret
  
```

'{{ image_pull_secret }}'
  
```
## postgres_sts
  
```

'{{ postgres_appname }}-sts'
  
```
## postgres_container
  
```

postgres
...
  
```
## postgres_container_group
  
```

'{{ postgres_container.replace(''-'', ''_'') }}'
  
```
## postgres_args
  
```

- '{{ ''run-postgresql-master'' if postgres_mode in [''readreplicas''] else ''run-postgresql''}}'
  
```
## postgres_startup_probe
  
```

true
...
  
```
## postgres_startup_command
  
```

'[''/usr/libexec/check-container-postgres'']'
  
```
## postgres_startup_initial
  
```

'{{ 5 if not postgres_upgrade else 30 }}'
  
```
## postgres_startup_period
  
```

'{{ 10 if not postgres_upgrade else 60 }}'
  
```
## postgres_startup_timeout
  
```

1
...
  
```
## postgres_startup_success
  
```

1
...
  
```
## postgres_startup_failure
  
```

'{{ 3 if not postgres_upgrade else postgres_upgrade_readiness_failure }}'
  
```
## postgres_readiness_probe
  
```

true
...
  
```
## postgres_readiness_command
  
```

'[''/usr/libexec/check-container-postgres'']'
  
```
## postgres_readiness_initial
  
```

5
...
  
```
## postgres_readiness_period
  
```

10
...
  
```
## postgres_readiness_timeout
  
```

1
...
  
```
## postgres_readiness_success
  
```

1
...
  
```
## postgres_readiness_failure
  
```

3
...
  
```
## postgres_liveness_probe
  
```

true
...
  
```
## postgres_liveness_command
  
```

'[''/usr/libexec/check-container-postgres'', ''--live'']'
  
```
## postgres_liveness_initial
  
```

120
...
  
```
## postgres_liveness_period
  
```

10
...
  
```
## postgres_liveness_timeout
  
```

10
...
  
```
## postgres_liveness_success
  
```

1
...
  
```
## postgres_liveness_failure
  
```

3
...
  
```
## postgres_resource_requests
  
```

true
...
  
```
## postgres_resource_requests_cpu
  
```

25m
...
  
```
## postgres_resource_requests_memory
  
```

64Mi
...
  
```
## postgres_resource_limits
  
```

false
...
  
```
## postgres_resource_limits_cpu
  
```

1
...
  
```
## postgres_resource_limits_memory
  
```

1Gi
...
  
```
## postgres_term_grace_period
  
```

30
...
  
```
## postgres_data
  
```

/var/lib/pgsql/data
...
  
```
## postgres_tolerations
  
```

false
...
  
```
## postgres_node_selector
  
```

false
...
  
```
## postgres_affinity
  
```

false
...
  
```
## postgres_port
  
```

5432
...
  
```
## postgres_readreplicas_size
  
```

1
...
  
```
## postgres_readreplicas_sts
  
```

'{{ postgres_readreplicas_appname }}-sts'
  
```
## postgres_readreplicas_args
  
```

- run-postgresql-slave
  
```
## postgres_readreplicas_container
  
```

postgres-readreplica
...
  
```
## postgres_readreplicas_container_group
  
```

'{{ postgres_readreplicas_container.replace(''-'', ''_'') }}'
  
```
## postgres_readreplicas_startup_probe
  
```

'{{ postgres_startup_probe }}'
  
```
## postgres_readreplicas_startup_command
  
```

'{{ postgres_startup_command }}'
  
```
## postgres_readreplicas_startup_initial
  
```

'{{ postgres_startup_initial }}'
  
```
## postgres_readreplicas_startup_period
  
```

'{{ postgres_startup_period }}'
  
```
## postgres_readreplicas_startup_timeout
  
```

'{{ postgres_startup_timeout }}'
  
```
## postgres_readreplicas_startup_success
  
```

'{{ postgres_startup_success }}'
  
```
## postgres_readreplicas_startup_failure
  
```

'{{ postgres_startup_failure }}'
  
```
## postgres_readreplicas_readiness_probe
  
```

'{{ postgres_readiness_probe }}'
  
```
## postgres_readreplicas_readiness_command
  
```

'{{ postgres_readiness_command }}'
  
```
## postgres_readreplicas_readiness_initial
  
```

'{{ postgres_readiness_initial }}'
  
```
## postgres_readreplicas_readiness_period
  
```

'{{ postgres_readiness_period }}'
  
```
## postgres_readreplicas_readiness_timeout
  
```

'{{ postgres_readiness_timeout }}'
  
```
## postgres_readreplicas_readiness_success
  
```

'{{ postgres_readiness_success }}'
  
```
## postgres_readreplicas_readiness_failure
  
```

'{{ postgres_readiness_failure }}'
  
```
## postgres_readreplicas_liveness_probe
  
```

'{{ postgres_liveness_probe }}'
  
```
## postgres_readreplicas_liveness_command
  
```

'{{ postgres_liveness_command }}'
  
```
## postgres_readreplicas_liveness_initial
  
```

'{{ postgres_liveness_initial }}'
  
```
## postgres_readreplicas_liveness_period
  
```

'{{ postgres_liveness_period }}'
  
```
## postgres_readreplicas_liveness_timeout
  
```

'{{ postgres_liveness_timeout }}'
  
```
## postgres_readreplicas_liveness_success
  
```

'{{ postgres_liveness_success }}'
  
```
## postgres_readreplicas_liveness_failure
  
```

'{{ postgres_liveness_failure }}'
  
```
## postgres_readreplicas_resource_requests
  
```

'{{ postgres_resource_requests }}'
  
```
## postgres_readreplicas_resource_requests_cpu
  
```

'{{ postgres_resource_requests_cpu }}'
  
```
## postgres_readreplicas_resource_requests_memory
  
```

'{{ postgres_resource_requests_memory }}'
  
```
## postgres_readreplicas_resource_limits
  
```

'{{ postgres_resource_limits }}'
  
```
## postgres_readreplicas_resource_limits_cpu
  
```

'{{ postgres_resource_limits_cpu }}'
  
```
## postgres_readreplicas_resource_limits_memory
  
```

'{{ postgres_resource_limits_memory }}'
  
```
## postgres_readreplicas_term_grace_period
  
```

'{{ postgres_term_grace_period }}'
  
```
## postgres_readreplicas_tolerations
  
```

'{{ postgres_tolerations }}'
  
```
## postgres_readreplicas_node_selector
  
```

'{{ postgres_node_selector }}'
  
```
## postgres_readreplicas_affinity
  
```

'{{ postgres_affinity }}'
  
```
## postgres_secret
  
```

'{{ postgres_appname }}-secret'
  
```
## postgres_database_name
  
```

'{{ lookup(''password'', ''/dev/null chars=ascii_lowercase length=8'') }}'
  
```
## postgres_database_user
  
```

'{{ lookup(''password'', ''/dev/null chars=ascii_lowercase length=8'') }}'
  
```
## postgres_database_password
  
```

'{{ lookup(''password'', ''/dev/null'') }}'
  
```
## postgres_database_master_user
  
```

'{{ lookup(''password'', ''/dev/null chars=ascii_lowercase length=8'') }}'
  
```
## postgres_database_master_password
  
```

'{{ lookup(''password'', ''/dev/null'') }}'
  
```
## postgres_secret_data
  
```

"database_name: {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=postgres_secret).data.database_name |\n  default(postgres_database_name\
  \ |\n  b64encode,true) }}\ndatabase_user: {{ lookup('k8s', api_version='v1', kind='Secret',\
  \ namespace=meta_namespace,\n  resource_name=postgres_secret).data.database_user\
  \ |\n  default(postgres_database_user |\n  b64encode,true) }}\ndatabase_password:\
  \ {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=postgres_secret).data.database_password |\n  default(postgres_database_password\
  \ |\n  b64encode,true) }}\ndatabase_url: {{ lookup('k8s', api_version='v1', kind='Secret',\
  \ namespace=meta_namespace,\n  resource_name=postgres_secret).data.database_url\
  \ |\n  default(('postgres://' + postgres_database_user + ':' + postgres_database_password\n\
  \  + '@' + postgres_service + ':' + postgres_port | string + '/' + postgres_database_name)\
  \ |\n  b64encode,true) }}\ndatabase_master_user: {{ lookup('k8s', api_version='v1',\
  \ kind='Secret', namespace=meta_namespace,\n  resource_name=postgres_secret).data.database_master_user\
  \ |\n  default(postgres_database_master_user |\n  b64encode,true) }}\ndatabase_master_password:\
  \ {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=postgres_secret).data.database_master_password |\n  default(postgres_database_master_password\
  \ |\n  b64encode,true) }}\n"
  
```
## postgres_service
  
```

'{{ postgres_appname }}-service'
  
```
## postgres_service_spec
  
```

"selector:\n  app: '{{ postgres_appname }}'\nclusterIP: None\nports:\n  - name: postgresql\n\
  \    port: {{ postgres_port }}\n    protocol: TCP\n    targetPort: {{ postgres_port\
  \ }}\nsessionAffinity: {{ postgres_service_session_affinity | default('None') }}\n\
  {% if postgres_service_session_affinity_timeout is defined %}\nsessionAffinityConfig:\n\
  \  clientIP:\n    timeoutSeconds: {{ postgres_service_session_affinity_timeout }}\n\
  {% endif %}\n"
  
```
## postgres_readreplicas_service
  
```

'{{ postgres_readreplicas_appname }}-service'
  
```
## postgres_readreplicas_service_spec
  
```

"selector:\n  app: '{{ postgres_readreplicas_appname }}'\nclusterIP: None\nports:\n\
  \  - name: postgresql\n    port: {{ postgres_port }}\n    protocol: TCP\n    targetPort:\
  \ {{ postgres_port }}\nsessionAffinity: {{ postgres_readreplicas_service_session_affinity\
  \ | default('None') }}\n{% if postgres_readreplicas_service_session_affinity_timeout\
  \ is defined %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ postgres_readreplicas_service_session_affinity_timeout\
  \ }}\n{% endif %}\n"
  
```
## postgres_readonly_service
  
```

'{{ postgres_readreplicas_appname }}-readonly-service'
  
```
## postgres_readonly_service_spec
  
```

"type: {{ postgres_service_type | default('ClusterIP') }}\nselector:\n{% if postgres_readonly_service_include_master\
  \ | default(true) | bool %}\n  app.kubernetes.io/part-of: \"{{ meta_name }}\"\n\
  {% else %}\n  app: '{{ postgres_readreplicas_appname }}'\n{% endif %}\nports:\n\
  \  - name: postgresql\n    port: {{ postgres_port }}\n    protocol: TCP\n    targetPort:\
  \ {{ postgres_port }}\nsessionAffinity: {{ postgres_service_session_affinity | default('None')\
  \ }}\n{% if postgres_service_session_affinity_timeout is defined %}\nsessionAffinityConfig:\n\
  \  clientIP:\n    timeoutSeconds: {{ postgres_service_session_affinity_timeout }}\n\
  {% endif %}\n"
  
```
## postgres_cm
  
```

'{{ postgres_appname }}-cm'
  
```
## postgres_cm_data
  
```

"postgres-extra.conf: |\n  {{ postgres_extra_config | default('') | indent(2) }}\n"
  
```
## postgres_cm_vars
  
```

'{{ postgres_appname }}-cm-vars'
  
```
## postgres_cm_vars_data
  
```

'POSTGRESQL_MAX_CONNECTIONS: "{{ postgres_max_connections | default(''100'') }}"

  POSTGRESQL_MAX_PREPARED_TRANSACTIONS: "{{ postgres_max_prepared_transactions | default(''0'')
  }}"

  POSTGRESQL_SHARED_BUFFERS: {{ postgres_shared_buffers | default(''32MB'') }}

  POSTGRESQL_EFFECTIVE_CACHE_SIZE: {{ postgres_effective_cache_size | default(''128MB'')
  }}

  # Replication

  POSTGRESQL_MAX_WAL_SENDERS: "{{ postgrespostgresql_max_wal_senders | default(''6'')
  }}"

  POSTGRESQL_WAL_KEEP_SIZE: "{{ postgres_wal_keep_size | default(''6000'') }}"

  # Recovery:

  POSTGRESQL_MASTER_SERVICE_NAME: "{{ postgres_service }}"

  '
  
```
## postgres_pvc_data
  
```

'{{ postgres_appname }}-data-pvc'
  
```
## postgres_pvc_data_storage_access_mode
  
```

ReadWriteOnce
...
  
```
## postgres_pvc_data_storage_class_name
  
```

false
...
  
```
## postgres_pvc_data_spec
  
```

"{% if postgres_pvc_data_storage_class_name is defined and postgres_pvc_data_storage_class_name\
  \ %}\nstorageClassName: {{ postgres_pvc_data_storage_class_name }}\n{% endif %}\n\
  accessModes:\n  - '{{ postgres_pvc_data_storage_access_mode }}'\nresources:\n  requests:\n\
  \    storage: '{{ postgres_pvc_data_size }}'\n"
  
```
## postgres_pvc_data_current_size
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=postgres_sts).spec.volumeClaimTemplates[0].spec.resources.requests.storage
  | default('''') }}'
  
```
## postgres_pvc_data_size
  
```

'{{ postgres_pvc_data_size_gib | string + ''Gi'' if postgres_pvc_data_autoexpansion
  else postgres_pvc_data_current_size | default(''1Gi'', true) }}'
  
```
## postgres_pvc_data_size_gib
  
```

'{{ cr_status_properties[routine_pvc_autoexpand_info_keyname].autoexpandSizeGib |
  default(postgres_pvc_data_autoexpansion_increment_gib) }}'
  
```
## postgres_pvc_data_autoexpansion
  
```

false
...
  
```
## postgres_pvc_data_autoexpansion_increment_gib
  
```

1
...
  
```
## postgres_pvc_data_autoexpansion_cap_gib
  
```

5
...
  
```
## postgres_pvc_data_current_labels
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=postgres_sts).spec.volumeClaimTemplates[0].metadata.labels | default('''')
  }}'
  
```
## postgres_readreplicas_pvc_data
  
```

'{{ postgres_readreplicas_appname }}-data-pvc'
  
```
## postgres_readreplicas_pvc_data_storage_access_mode
  
```

'{{ postgres_pvc_data_storage_access_mode }}'
  
```
## postgres_readreplicas_pvc_data_storage_class_name
  
```

'{{ postgres_pvc_data_storage_class_name }}'
  
```
## postgres_readreplicas_pvc_data_spec
  
```

'{{ postgres_pvc_data_spec }}'
  
```
## postgres_readreplicas_pvc_data_current_size
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=postgres_readreplicas_sts).spec.volumeClaimTemplates[0].spec.resources.requests.storage
  | default('''') }}'
  
```
## postgres_readreplicas_pvc_data_size
  
```

'{{ postgres_readreplicas_pvc_data_size_gib | string + ''Gi'' if postgres_readreplicas_pvc_data_autoexpansion
  else postgres_readreplicas_pvc_data_current_size | default(postgres_pvc_data_size)
  }}'
  
```
## postgres_readreplicas_pvc_data_size_gib
  
```

'{{ cr_status_properties[routine_pvc_autoexpand_info_keyname].autoexpandSizeGib |
  default(postgres_readreplicas_pvc_data_autoexpansion_increment_gib) }}'
  
```
## postgres_readreplicas_pvc_data_autoexpansion
  
```

false
...
  
```
## postgres_readreplicas_pvc_data_autoexpansion_increment_gib
  
```

1
...
  
```
## postgres_readreplicas_pvc_data_autoexpansion_cap_gib
  
```

5
...
  
```
## postgres_readreplicas_pvc_data_current_labels
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=postgres_readreplicas_sts).spec.volumeClaimTemplates[0].metadata.labels
  | default('''') }}'
  
```
## postgres_upgrade
  
```

false
...
  
```
## postgres_upgrade_readiness_failure
  
```

10
...
  
```
## postgres_config_log_stderr
  
```

true
...
  
```
## postgres_vpa
  
```

'{{ postgres_appname }}-vpa'
  
```
## postgres_vpa_spec
  
```

false
...
  
```
## postgres_readreplicas_vpa
  
```

'{{ postgres_readreplicas_appname }}-vpa'
  
```
## postgres_readreplicas_vpa_spec
  
```

false
...
  
```




# keydb.yml
  
---
## keydb_state
  
```

'{{ state }}'
  
```
## keydb_appname
  
```

'{{ meta_name }}-keydb'
  
```
## keydb_mode
  
```

standalone
...
  
```
## keydb_size
  
```

1
...
  
```
## keydb_image
  
```

quay.io/krestomatio/keydb:6.3.4@sha256:80582cafaa6bd418e6b4ba32d0a45f839652fa33342dd5b8f4e369c78b0f562f
...
  
```
## keydb_image_pull_secret
  
```

'{{ image_pull_secret }}'
  
```
## keydb_sts
  
```

'{{ keydb_appname }}-sts'
  
```
## keydb_args
  
```

- --requirepass "$(KEYDB_PASSWORD)"
  
```
## keydb_container
  
```

keydb
...
  
```
## keydb_container_group
  
```

'{{ keydb_container.replace(''-'', ''_'') }}'
  
```
## keydb_startup_probe
  
```

true
...
  
```
## keydb_startup_command
  
```

'[''/usr/libexec/check-container-keydb'', ''-r'']'
  
```
## keydb_startup_initial
  
```

0
...
  
```
## keydb_startup_period
  
```

15
...
  
```
## keydb_startup_timeout
  
```

3
...
  
```
## keydb_startup_success
  
```

1
...
  
```
## keydb_startup_failure
  
```

12
...
  
```
## keydb_readiness_probe
  
```

true
...
  
```
## keydb_readiness_command
  
```

'[''/usr/libexec/check-container-keydb'', ''-r'']'
  
```
## keydb_readiness_initial
  
```

0
...
  
```
## keydb_readiness_period
  
```

15
...
  
```
## keydb_readiness_timeout
  
```

3
...
  
```
## keydb_readiness_success
  
```

1
...
  
```
## keydb_readiness_failure
  
```

3
...
  
```
## keydb_liveness_probe
  
```

true
...
  
```
## keydb_liveness_command
  
```

'[''/usr/libexec/check-container-keydb'', ''-l'']'
  
```
## keydb_liveness_initial
  
```

0
...
  
```
## keydb_liveness_period
  
```

15
...
  
```
## keydb_liveness_timeout
  
```

3
...
  
```
## keydb_liveness_success
  
```

1
...
  
```
## keydb_liveness_failure
  
```

6
...
  
```
## keydb_resource_requests
  
```

true
...
  
```
## keydb_resource_requests_cpu
  
```

25m
...
  
```
## keydb_resource_requests_memory
  
```

64Mi
...
  
```
## keydb_resource_limits
  
```

false
...
  
```
## keydb_resource_limits_cpu
  
```

1
...
  
```
## keydb_resource_limits_memory
  
```

1Gi
...
  
```
## keydb_term_grace_period
  
```

30
...
  
```
## keydb_data
  
```

/data
...
  
```
## keydb_tolerations
  
```

false
...
  
```
## keydb_node_selector
  
```

false
...
  
```
## keydb_affinity
  
```

false
...
  
```
## keydb_port
  
```

6379
...
  
```
## keydb_service
  
```

'{{ keydb_appname }}-service'
  
```
## keydb_service_spec
  
```

"type: {{ keydb_service_type | default('ClusterIP') }}\nselector:\n  app: '{{ keydb_appname\
  \ }}'\nports:\n  - name: keydb\n    port: {{ keydb_port }}\n    protocol: TCP\n\
  \    targetPort: {{ keydb_port }}\nsessionAffinity: {{ keydb_service_session_affinity\
  \ | default('None') }}\n{% if keydb_service_session_affinity_timeout is defined\
  \ %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ keydb_service_session_affinity_timeout\
  \ }}\n{% endif %}\n"
  
```
## keydb_service_headless
  
```

'{{ keydb_appname }}-headless'
  
```
## keydb_service_headless_spec
  
```

"selector:\n  app: '{{ keydb_appname }}'\nclusterIP: None\nports:\n  - name: keydb\n\
  \    port: {{ keydb_port }}\n    protocol: TCP\n    targetPort: {{ keydb_port }}\n\
  sessionAffinity: {{ keydb_service_session_affinity | default('None') }}\n{% if keydb_service_session_affinity_timeout\
  \ is defined %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ keydb_service_session_affinity_timeout\
  \ }}\n{% endif %}\n"
  
```
## keydb_pvc_data
  
```

'{{ keydb_appname }}-data-pvc'
  
```
## keydb_pvc_data_storage_access_mode
  
```

ReadWriteOnce
...
  
```
## keydb_pvc_data_storage_class_name
  
```

false
...
  
```
## keydb_pvc_data_spec
  
```

"{% if keydb_pvc_data_storage_class_name is defined and keydb_pvc_data_storage_class_name\
  \ %}\nstorageClassName: {{ keydb_pvc_data_storage_class_name }}\n{% endif %}\naccessModes:\n\
  \  - '{{ keydb_pvc_data_storage_access_mode }}'\nresources:\n  requests:\n    storage:\
  \ '{{ keydb_pvc_data_size }}'\n"
  
```
## keydb_pvc_data_current_size
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=keydb_sts).spec.volumeClaimTemplates[0].spec.resources.requests.storage
  | default('''') }}'
  
```
## keydb_pvc_data_size
  
```

'{{ keydb_pvc_data_size_gib | string + ''Gi'' if keydb_pvc_data_autoexpansion else
  keydb_pvc_data_current_size | default(''1Gi'', true) }}'
  
```
## keydb_pvc_data_size_gib
  
```

'{{ cr_status_properties[routine_pvc_autoexpand_info_keyname].autoexpandSizeGib |
  default(keydb_pvc_data_autoexpansion_increment_gib) }}'
  
```
## keydb_pvc_data_autoexpansion
  
```

false
...
  
```
## keydb_pvc_data_autoexpansion_increment_gib
  
```

1
...
  
```
## keydb_pvc_data_autoexpansion_cap_gib
  
```

5
...
  
```
## keydb_pvc_data_current_labels
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=keydb_sts).spec.volumeClaimTemplates[0].metadata.labels | default('''')
  }}'
  
```
## keydb_secret
  
```

'{{ keydb_appname }}-secret'
  
```
## keydb_password
  
```

'{{ lookup(''password'', ''/dev/null'') }}'
  
```
## keydb_secret_data
  
```

"keydb_password: {{ lookup('k8s', api_version='v1', kind='Secret', namespace=meta_namespace,\n\
  \  resource_name=keydb_secret).data.keydb_password |\n  default(keydb_password |\n\
  \  b64encode,true) }}\n"
  
```
## keydb_cm
  
```

'{{ keydb_appname }}-cm'
  
```
## keydb_cm_data_config
  
```

'port {{ keydb_port }}

  dir {{ keydb_data }}

  server-threads {{ keydb_config_server_threads | default(''2'') }}

  tcp-keepalive 60

  save 900 1

  save 300 10

  {% if keydb_extra_config is defined and keydb_extra_config %}

  # keydb extra config

  {{ keydb_extra_config }}

  {% endif %}

  {% if keydb_mode_config is defined and keydb_mode_config %}

  # keydb mode: {{ keydb_mode }}

  {{ keydb_mode_config }}

  {% endif %}

  '
  
```
## keydb_cm_data
  
```

"keydb.conf: |\n  {{ keydb_cm_data_config | indent(2) }}\n"
  
```
## keydb_vpa
  
```

'{{ keydb_appname }}-vpa'
  
```
## keydb_vpa_spec
  
```

false
...
  
```
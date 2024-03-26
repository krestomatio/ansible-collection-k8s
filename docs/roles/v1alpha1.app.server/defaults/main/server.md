



# server.yml
  
---
## server_state
  
```

'{{ state }}'
  
```
## server_appname
  
```

'{{ meta_name }}-server'
  
```
## server_size
  
```

1
...
  
```
## server_image
  
```

hasura/k8s-stack-event-triggers:6c3a63c
...
  
```
## server_image_pull_secret
  
```

'{{ image_pull_secret }}'
  
```
## server_deploy
  
```

'{{ server_appname }}-deploy'
  
```
## server_port
  
```

3000
...
  
```
## server_host
  
```

'{{ server_ingress_host }}'
  
```
## server_args
  
```

'[''npm'', ''run'', ''start-prod'']'
  
```
## server_container
  
```

server
...
  
```
## server_container_group
  
```

'{{ server_container.replace(''-'', ''_'') }}'
  
```
## server_readiness_probe
  
```

false
...
  
```
## server_readiness_path
  
```

/healthz
...
  
```
## server_readiness_initial
  
```

5
...
  
```
## server_readiness_period
  
```

30
...
  
```
## server_readiness_timeout
  
```

3
...
  
```
## server_readiness_success
  
```

1
...
  
```
## server_readiness_failure
  
```

6
...
  
```
## server_liveness_probe
  
```

false
...
  
```
## server_liveness_path
  
```

/healthz
...
  
```
## server_liveness_initial
  
```

5
...
  
```
## server_liveness_period
  
```

10
...
  
```
## server_liveness_timeout
  
```

3
...
  
```
## server_liveness_success
  
```

1
...
  
```
## server_liveness_failure
  
```

3
...
  
```
## server_resource_requests
  
```

true
...
  
```
## server_resource_requests_cpu
  
```

25m
...
  
```
## server_resource_requests_memory
  
```

64Mi
...
  
```
## server_resource_limits
  
```

false
...
  
```
## server_resource_limits_cpu
  
```

1
...
  
```
## server_resource_limits_memory
  
```

1Gi
...
  
```
## server_term_grace_period
  
```

30
...
  
```
## server_run_as_user
  
```

1001
...
  
```
## server_tolerations
  
```

false
...
  
```
## server_connects_to
  
```

'{{ server_database_appname if server_database_deploy else false }}'
  
```
## server_automount_service_account_token
  
```

false
...
  
```
## server_service
  
```

'{{ server_appname }}-service'
  
```
## server_service_type
  
```

ClusterIP
...
  
```
## server_service_spec
  
```

"type: {{ server_service_type }}\nsessionAffinity: {{ server_service_session_affinity\
  \ | default('None') }}\n{% if server_service_session_affinity_timeout is defined\
  \ %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ server_service_session_affinity_timeout\
  \ }}\n{% endif %}\nports:\n- name: http\n  port: {{ server_port }}\n  protocol:\
  \ TCP\n  targetPort: {{ server_port }}\nselector:\n  app: '{{ server_appname }}'\n"
  
```
## server_ingress
  
```

'{{ server_appname }}-ingress'
  
```
## server_ingress_deploy
  
```

false
...
  
```
## server_ingress_type
  
```

'{{ ''route'' if (k8s_distribution | default(''k8s'')) == ''okd'' else ''ingress''
  }}'
  
```
## server_ingress_tls
  
```

'{{ true if server_ingress_protocol == ''https'' else false }}'
  
```
## server_ingress_protocol
  
```

http
...
  
```
## server_ingress_host
  
```

example.krestomat.io
...
  
```
## server_ingress_tls_secret_name
  
```

'{{ server_ingress + ''-tls'' if server_ingress_annotations | default('''') is regex(''cert-manager.io/(cluster-|)issuer:(?!
  null)'') else '''' }}'
  
```
## server_ingress_spec
  
```

"{% if server_ingress_tls %}\ntls:\n- hosts:\n  - '{{ server_host }}'\n{% if server_ingress_tls_secret_name\
  \ != '' %}\n  secretName: {{ server_ingress_tls_secret_name }}\n{% endif %}\n{%\
  \ endif %}\nrules:\n- host: '{{ server_host }}'\n  http:\n    paths:\n    - path:\
  \ {{ server_ingress_path | default('/') }}\n      pathType: {{ server_ingress_path_type\
  \ | default('ImplementationSpecific') }}\n      backend:\n        service:\n   \
  \       name: '{{ server_service }}'\n          port:\n            number: {{ server_port\
  \ }}\n"
  
```
## server_route
  
```

'{{ server_appname }}-route'
  
```
## server_route_tls
  
```

'{{ server_ingress_tls }}'
  
```
## server_route_annotations
  
```

'haproxy.router.openshift.io/rate-limit-connections: ''true''

  haproxy.router.openshift.io/rate-limit-connections.concurrent-tcp: ''100''

  haproxy.router.openshift.io/rate-limit-connections.rate-http: ''100''

  haproxy.router.openshift.io/rate-limit-connections.rate-tcp: ''100''

  '
  
```
## server_route_spec
  
```

"host: '{{ server_host }}'\nto:\n  kind: Service\n  name: '{{ server_service }}'\n\
  \  weight: 100\nport:\n  targetPort: http\n{% if server_route_tls %}\ntls:\n  termination:\
  \ edge\n  insecureEdgeTerminationPolicy: Redirect\n{% endif %}\nwildcardPolicy:\
  \ None\n"
  
```
## server_secret_handler
  
```

false
...
  
```
## server_database_deploy
  
```

false
...
  
```
## server_database_appname
  
```

'{{ postgres_appname | default(meta_name + ''-postgres'') }}'
  
```
## server_database_service
  
```

'{{ postgres_service | default(server_database_appname + ''-service'') }}'
  
```
## server_database_secret
  
```

'{{ postgres_secret | default(server_database_appname + ''-secret'') if server_database_deploy
  else false }}'
  
```
## server_database_secret_dbname_key
  
```

database_name
...
  
```
## server_database_secret_dbuser_key
  
```

database_user
...
  
```
## server_database_secret_dbpass_key
  
```

database_password
...
  
```
## server_database_secret_dburl_key
  
```

database_url
...
  
```
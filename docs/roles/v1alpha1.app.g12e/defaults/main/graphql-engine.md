



# graphql-engine.yml

---
## graphql_engine_state

```

'{{ state }}'

```
## graphql_engine_appname

```

'{{ meta_name }}-graphql-engine'

```
## graphql_engine_size

```

1
...

```
## graphql_engine_image

```

quay.io/krestomatio/graphql-engine@sha256:b612c3e3da62252ece5cb2e468fafd7e6d73e5c430793ddd3bd5cbf4a9ac343f
...

```
## graphql_engine_image_pull_secret

```

'{{ image_pull_secret }}'

```
## graphql_engine_deploy

```

'{{ graphql_engine_appname }}-deploy'

```
## graphql_engine_port

```

8080
...

```
## graphql_engine_host

```

'{{ graphql_engine_ingress_host }}'

```
## graphql_engine_args

```

'[''graphql-engine'',''serve'']'

```
## graphql_engine_container

```

graphql-engine
...

```
## graphql_engine_container_group

```

'{{ graphql_engine_container.replace(''-'', ''_'') }}'

```
## graphql_engine_readiness_probe

```

true
...

```
## graphql_engine_readiness_path

```

/healthz
...

```
## graphql_engine_readiness_initial

```

5
...

```
## graphql_engine_readiness_period

```

30
...

```
## graphql_engine_readiness_timeout

```

3
...

```
## graphql_engine_readiness_success

```

1
...

```
## graphql_engine_readiness_failure

```

6
...

```
## graphql_engine_liveness_probe

```

true
...

```
## graphql_engine_liveness_path

```

/healthz
...

```
## graphql_engine_liveness_initial

```

5
...

```
## graphql_engine_liveness_period

```

10
...

```
## graphql_engine_liveness_timeout

```

3
...

```
## graphql_engine_liveness_success

```

1
...

```
## graphql_engine_liveness_failure

```

3
...

```
## graphql_engine_resource_requests

```

true
...

```
## graphql_engine_resource_requests_cpu

```

25m
...

```
## graphql_engine_resource_requests_memory

```

64Mi
...

```
## graphql_engine_resource_limits

```

false
...

```
## graphql_engine_resource_limits_cpu

```

1
...

```
## graphql_engine_resource_limits_memory

```

1Gi
...

```
## graphql_engine_term_grace_period

```

30
...

```
## graphql_engine_run_as_user

```

1001
...

```
## graphql_engine_tolerations

```

false
...

```
## graphql_engine_connects_to

```

'{{ graphql_engine_database_appname if graphql_engine_database_deploy else false }}'

```
## graphql_engine_service

```

'{{ graphql_engine_appname }}-service'

```
## graphql_engine_service_type

```

ClusterIP
...

```
## graphql_engine_service_spec

```

"type: {{ graphql_engine_service_type }}\nsessionAffinity: {{ graphql_engine_service_session_affinity\
  \ | default('None') }}\n{% if graphql_engine_service_session_affinity_timeout is\
  \ defined %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ graphql_engine_service_session_affinity_timeout\
  \ }}\n{% endif %}\nports:\n- name: http\n  port: {{ graphql_engine_port }}\n  protocol:\
  \ TCP\n  targetPort: {{ graphql_engine_port }}\nselector:\n  app: '{{ graphql_engine_appname\
  \ }}'\n"

```
## graphql_engine_ingress

```

'{{ graphql_engine_appname }}-ingress'

```
## graphql_engine_ingress_type

```

'{{ ''route'' if (k8s_distribution | default(''k8s'')) == ''okd'' else ''ingress''
  }}'

```
## graphql_engine_ingress_tls

```

'{{ true if graphql_engine_ingress_protocol == ''https'' else false }}'

```
## graphql_engine_ingress_protocol

```

http
...

```
## graphql_engine_ingress_host

```

example.krestomat.io
...

```
## graphql_engine_ingress_tls_secret_name

```

'{{ graphql_engine_ingress + ''-tls'' if graphql_engine_ingress_annotations | default('''')
  is regex(''cert-manager.io/(cluster-|)issuer:(?! null)'') else '''' }}'

```
## graphql_engine_ingress_spec

```

"{% if graphql_engine_ingress_tls %}\ntls:\n- hosts:\n  - '{{ graphql_engine_host\
  \ }}'\n{% if graphql_engine_ingress_tls_secret_name != '' %}\n  secretName: {{ graphql_engine_ingress_tls_secret_name\
  \ }}\n{% endif %}\n{% endif %}\nrules:\n- host: '{{ graphql_engine_host }}'\n  http:\n\
  \    paths:\n    - path: {{ graphql_engine_ingress_path | default('/') }}\n    \
  \  pathType: {{ graphql_engine_ingress_path_type | default('ImplementationSpecific')\
  \ }}\n      backend:\n        service:\n          name: '{{ graphql_engine_service\
  \ }}'\n          port:\n            number: {{ graphql_engine_port }}\n"

```
## graphql_engine_route

```

'{{ graphql_engine_appname }}-route'

```
## graphql_engine_route_tls

```

'{{ graphql_engine_ingress_tls }}'

```
## graphql_engine_route_annotations

```

'haproxy.router.openshift.io/rate-limit-connections: ''true''

  haproxy.router.openshift.io/rate-limit-connections.concurrent-tcp: ''100''

  haproxy.router.openshift.io/rate-limit-connections.rate-http: ''100''

  haproxy.router.openshift.io/rate-limit-connections.rate-tcp: ''100''

  '

```
## graphql_engine_route_spec

```

"host: '{{ graphql_engine_host }}'\nto:\n  kind: Service\n  name: '{{ graphql_engine_service\
  \ }}'\n  weight: 100\nport:\n  targetPort: http\n{% if graphql_engine_route_tls\
  \ %}\ntls:\n  termination: edge\n  insecureEdgeTerminationPolicy: Redirect\n{% endif\
  \ %}\nwildcardPolicy: None\n"

```
## graphql_engine_secret_handler

```

'{{ graphql_engine_appname }}-secret-handler'

```
## graphql_engine_secret_handler_key

```

GRAPHQL_ENGINE_HANDLER_SECRET
...

```
## graphql_engine_secret_handler_data

```

'{{ graphql_engine_secret_handler_key }}: {{ lookup(''k8s'', api_version=''v1'', kind=''Secret'',

  namespace=meta_namespace, resource_name=graphql_engine_secret_handler).data[graphql_engine_secret_handler_key]

  | default(lookup(''password'', ''/dev/null'') | b64encode,true) }}

  '

```
## graphql_engine_database_deploy

```

true
...

```
## graphql_engine_database_appname

```

'{{ postgres_appname | default(meta_name + ''-postgres'') }}'

```
## graphql_engine_database_service

```

'{{ postgres_service | default(graphql_engine_database_appname + ''-service'') }}'

```
## graphql_engine_database_secret

```

'{{ postgres_secret | default(graphql_engine_database_appname + ''-secret'') }}'

```
## graphql_engine_database_secret_dbname_key

```

database_name
...

```
## graphql_engine_database_secret_dbuser_key

```

database_user
...

```
## graphql_engine_database_secret_dbpass_key

```

database_password
...

```
## graphql_engine_database_secret_dburl_key

```

database_url
...

```
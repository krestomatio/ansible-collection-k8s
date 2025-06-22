



# nginx.yml

---
## nginx_state

```

'{{ state }}'

```
## nginx_appname

```

'{{ meta_name }}-nginx'

```
## nginx_size

```

1
...

```
## nginx_image

```

quay.io/krestomatio/nginx:1.26@sha256:9980b0d28899bdea5ba00d6021e3d7fccaa22bc1bcdbc32b38294d1a86d6ae26
...

```
## nginx_image_pull_secret

```

'{{ image_pull_secret }}'

```
## nginx_deploy

```

'{{ nginx_appname }}-deploy'

```
## nginx_port

```

8080
...

```
## nginx_host

```

'{{ nginx_ingress_host }}'

```
## nginx_args

```

'[''nginx'']'

```
## nginx_container

```

nginx
...

```
## nginx_container_group

```

'{{ nginx_container.replace(''-'', ''_'') }}'

```
## nginx_startup_probe

```

false
...

```
## nginx_startup_path

```

/login/index.php
...

```
## nginx_startup_host

```

'{{ nginx_host }}'

```
## nginx_startup_port

```

'{{ nginx_port }}'

```
## nginx_startup_initial

```

5
...

```
## nginx_startup_period

```

10
...

```
## nginx_startup_timeout

```

3
...

```
## nginx_startup_success

```

1
...

```
## nginx_startup_failure

```

6
...

```
## nginx_readiness_probe

```

false
...

```
## nginx_readiness_path

```

/login/index.php
...

```
## nginx_readiness_host

```

'{{ nginx_host }}'

```
## nginx_readiness_port

```

'{{ nginx_port }}'

```
## nginx_readiness_initial

```

5
...

```
## nginx_readiness_period

```

10
...

```
## nginx_readiness_timeout

```

3
...

```
## nginx_readiness_success

```

1
...

```
## nginx_readiness_failure

```

6
...

```
## nginx_liveness_probe

```

false
...

```
## nginx_liveness_path

```

/login/index.php
...

```
## nginx_liveness_host

```

'{{ nginx_host }}'

```
## nginx_liveness_port

```

'{{ nginx_port }}'

```
## nginx_liveness_initial

```

5
...

```
## nginx_liveness_period

```

10
...

```
## nginx_liveness_timeout

```

3
...

```
## nginx_liveness_success

```

1
...

```
## nginx_liveness_failure

```

3
...

```
## nginx_resource_requests

```

true
...

```
## nginx_resource_requests_cpu

```

15m
...

```
## nginx_resource_requests_memory

```

32Mi
...

```
## nginx_resource_limits

```

false
...

```
## nginx_resource_limits_cpu

```

1
...

```
## nginx_resource_limits_memory

```

1Gi
...

```
## nginx_term_grace_period

```

30
...

```
## nginx_run_as_user

```

1001
...

```
## nginx_tolerations

```

false
...

```
## nginx_node_selector

```

false
...

```
## nginx_affinity

```

false
...

```
## nginx_connects_to

```

false
...

```
## nginx_cm

```

'{{ nginx_appname }}-cm'

```
## nginx_cm_data

```

"nginx-extra.conf: |\n  {{ nginx_extra_config | default('') | indent(2) }}\n"

```
## nginx_service

```

'{{ nginx_appname }}-service'

```
## nginx_service_type

```

ClusterIP
...

```
## nginx_service_spec

```

"type: {{ nginx_service_type }}\nsessionAffinity: {{ nginx_service_session_affinity\
  \ | default('None') }}\n{% if nginx_service_session_affinity_timeout is defined\
  \ %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ nginx_service_session_affinity_timeout\
  \ }}\n{% endif %}\nports:\n- name: http\n  port: {{ nginx_port }}\n  protocol: TCP\n\
  \  targetPort: {{ nginx_port }}\nselector:\n  app: '{{ nginx_appname }}'\n"

```
## nginx_ingress

```

'{{ nginx_appname }}-ingress'

```
## nginx_ingress_type

```

'{{ ''route'' if (k8s_distribution | default(''k8s'')) == ''okd'' else ''ingress''
  }}'

```
## nginx_ingress_tls

```

'{{ true if nginx_ingress_protocol == ''https'' else false }}'

```
## nginx_ingress_protocol

```

http
...

```
## nginx_ingress_host

```

example.krestomat.io
...

```
## nginx_ingress_only

```

false
...

```
## nginx_ingress_tls_secret_name

```

'{{ nginx_ingress + ''-tls'' if nginx_ingress_annotations | default('''') is regex(''cert-manager.io/(cluster-|)issuer:(?!
  null)'') else '''' }}'

```
## nginx_ingress_spec

```

"{% if nginx_ingress_tls %}\ntls:\n- hosts:\n  - '{{ nginx_host }}'\n{% if nginx_ingress_tls_secret_name\
  \ != '' %}\n  secretName: {{ nginx_ingress_tls_secret_name }}\n{% endif %}\n{% endif\
  \ %}\nrules:\n- host: '{{ nginx_host }}'\n  http:\n    paths:\n    - path: {{ nginx_ingress_path\
  \ | default('/') }}\n      pathType: {{ nginx_ingress_path_type | default('ImplementationSpecific')\
  \ }}\n      backend:\n        service:\n          name: '{{ nginx_service }}'\n\
  \          port:\n            number: {{ nginx_port }}\n"

```
## nginx_route

```

'{{ nginx_appname }}-route'

```
## nginx_route_tls

```

'{{ nginx_ingress_tls }}'

```
## nginx_route_only

```

false
...

```
## nginx_route_annotations

```

'haproxy.router.openshift.io/rate-limit-connections: ''true''

  haproxy.router.openshift.io/rate-limit-connections.concurrent-tcp: ''100''

  haproxy.router.openshift.io/rate-limit-connections.rate-http: ''100''

  haproxy.router.openshift.io/rate-limit-connections.rate-tcp: ''100''

  '

```
## nginx_route_spec

```

"host: '{{ nginx_host }}'\nto:\n  kind: Service\n  name: '{{ nginx_service }}'\n \
  \ weight: 100\nport:\n  targetPort: http\n{% if nginx_route_tls %}\ntls:\n  termination:\
  \ edge\n  insecureEdgeTerminationPolicy: Redirect\n{% endif %}\nwildcardPolicy:\
  \ None\n"

```
## nginx_hpa

```

'{{ nginx_appname }}-hpa'

```
## nginx_hpa_spec

```

false
...

```
## nginx_vpa

```

'{{ nginx_appname }}-vpa'

```
## nginx_vpa_spec

```

false
...

```
## nginx_netpol_omit

```

true
...

```
## nginx_netpol

```

'{{ nginx_appname }}-netpol'

```
## nginx_netpol_ingress_ipblock

```

false
...

```
## nginx_netpol_egress_ipblock

```

false
...

```
## nginx_netpol_connects_to

```

'{{ nginx_connects_to if nginx_connects_to | type_debug == ''list'' else [nginx_connects_to
  | default('''')] }}'

```
## nginx_netpol_spec

```

"policyTypes:\n- Ingress\n- Egress\npodSelector:\n  matchLabels:\n    app.kubernetes.io/name:\
  \ '{{ nginx_appname }}'\ningress:\n- ports:\n  - protocol: TCP\n    port: {{ nginx_port\
  \ }}\n- from:\n  - podSelector:\n      matchLabels:\n        {{ meta_app_connects_to\
  \ }}/{{ nginx_appname }}: 'true'\n{% if nginx_netpol_ingress_ipblock is defined\
  \ and nginx_netpol_ingress_ipblock %}\n  - ipBlock:\n      cidr: '{{ nginx_netpol_ingress_ipblock\
  \ }}'\n{% endif %}\negress:\n- ports:\n  - protocol: TCP\n    port: 53\n  - protocol:\
  \ UDP\n    port: 53\n  - protocol: TCP\n    port: 80\n  - protocol: TCP\n    port:\
  \ 443\n{% for nginx_netpol_connects_to_app_name in nginx_netpol_connects_to if nginx_netpol_connects_to_app_name\
  \ %}\n- to:\n  - podSelector:\n      matchLabels:\n        app.kubernetes.io/name:\
  \ '{{ nginx_netpol_connects_to_app_name }}'\n  - namespaceSelector:\n      matchLabels:\n\
  \        app.kubernetes.io/name: '{{ nginx_netpol_connects_to_app_name }}'\n   \
  \ podSelector:\n      matchLabels:\n        app.kubernetes.io/name: '{{ nginx_netpol_connects_to_app_name\
  \ }}'\n{% endfor %}\n{% if nginx_netpol_egress_ipblock is defined and nginx_netpol_egress_ipblock\
  \ %}\n  - ipBlock:\n      cidr: '{{ nginx_netpol_egress_ipblock }}'\n{% endif %}"

```
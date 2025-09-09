



# php-fpm.yml

---
## php_fpm_state

```

'{{ state }}'

```
## php_fpm_appname

```

'{{ meta_name }}-php-fpm'

```
## php_fpm_size

```

1
...

```
## php_fpm_image

```

quay.io/krestomatio/php-fpm@sha256:f8c03f70b0c15a27be37e0a71c4dc7d186a8053f613e7f44e67263cbf297212e
...

```
## php_fpm_image_pull_secret

```

'{{ image_pull_secret }}'

```
## php_fpm_deploy

```

'{{ php_fpm_appname }}-deploy'

```
## php_fpm_port

```

9000
...

```
## php_fpm_args

```

'[''php-fpm'']'

```
## php_fpm_container

```

php-fpm
...

```
## php_fpm_container_group

```

'{{ php_fpm_container.replace(''-'', ''_'') }}'

```
## php_fpm_startup_probe

```

false
...

```
## php_fpm_startup_command

```

'[''{{ php_fpm_check_container_script }}'', ''-s'']'

```
## php_fpm_startup_initial

```

5
...

```
## php_fpm_startup_period

```

10
...

```
## php_fpm_startup_timeout

```

3
...

```
## php_fpm_startup_success

```

1
...

```
## php_fpm_startup_failure

```

6
...

```
## php_fpm_readiness_probe

```

false
...

```
## php_fpm_readiness_command

```

'[''{{ php_fpm_check_container_script }}'', ''-r'']'

```
## php_fpm_readiness_initial

```

5
...

```
## php_fpm_readiness_period

```

10
...

```
## php_fpm_readiness_timeout

```

3
...

```
## php_fpm_readiness_success

```

1
...

```
## php_fpm_readiness_failure

```

6
...

```
## php_fpm_liveness_probe

```

false
...

```
## php_fpm_liveness_command

```

'[''{{ php_fpm_check_container_script }}'', ''-l'']'

```
## php_fpm_liveness_initial

```

5
...

```
## php_fpm_liveness_period

```

10
...

```
## php_fpm_liveness_timeout

```

3
...

```
## php_fpm_liveness_success

```

1
...

```
## php_fpm_liveness_failure

```

3
...

```
## php_fpm_check_container_script

```

/usr/libexec/check-container-php
...

```
## php_fpm_resource_requests

```

true
...

```
## php_fpm_resource_requests_cpu

```

15m
...

```
## php_fpm_resource_requests_memory

```

32Mi
...

```
## php_fpm_resource_limits

```

false
...

```
## php_fpm_resource_limits_cpu

```

1
...

```
## php_fpm_resource_limits_memory

```

1Gi
...

```
## php_fpm_term_grace_period

```

30
...

```
## php_fpm_tolerations

```

false
...

```
## php_fpm_node_selector

```

false
...

```
## php_fpm_affinity

```

false
...

```
## php_fpm_connects_to

```

false
...

```
## php_fpm_cm

```

'{{ php_fpm_appname }}-cm'

```
## php_fpm_cm_data

```

"php-extra.ini: |\n  {{ php_fpm_php_extra_ini | indent(2) }}\nphp-fpm-extra.conf:\
  \ |\n  {{ php_fpm_extra_config | indent(2) }}\n"

```
## php_fpm_php_extra_ini

```

''

```
## php_fpm_extra_config

```

''

```
## php_fpm_service

```

'{{ php_fpm_appname }}-service'

```
## php_fpm_service_type

```

ClusterIP
...

```
## php_fpm_service_spec

```

"type: {{ php_fpm_service_type }}\nsessionAffinity: {{ php_fpm_service_session_affinity\
  \ | default('None') }}\n{% if php_fpm_service_session_affinity_timeout is defined\
  \ %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ php_fpm_service_session_affinity_timeout\
  \ }}\n{% endif %}\nports:\n- name: http\n  port: {{ php_fpm_port }}\n  protocol:\
  \ TCP\n  targetPort: {{ php_fpm_port }}\nselector:\n  app: '{{ php_fpm_appname }}'\n"

```
## php_fpm_hpa

```

'{{ php_fpm_appname }}-hpa'

```
## php_fpm_hpa_spec

```

false
...

```
## php_fpm_vpa

```

'{{ php_fpm_appname }}-vpa'

```
## php_fpm_vpa_spec

```

false
...

```
## php_fpm_netpol_omit

```

true
...

```
## php_fpm_netpol

```

'{{ php_fpm_appname }}-netpol'

```
## php_fpm_netpol_ingress_ipblock

```

false
...

```
## php_fpm_netpol_egress_ipblock

```

false
...

```
## php_fpm_netpol_connects_to

```

'{{ php_fpm_connects_to if php_fpm_connects_to | type_debug == ''list'' else [php_fpm_connects_to
  | default('''')] }}'

```
## php_fpm_netpol_spec

```

"policyTypes:\n- Ingress\n- Egress\npodSelector:\n  matchLabels:\n    app.kubernetes.io/runtime:\
  \ 'php-fpm'\ningress:\n{% if php_fpm_netpol_ingress_extra_ports | default([]) %}\n\
  - ports:\n{% for _extra_port in php_fpm_netpol_ingress_extra_ports %}\n  - protocol:\
  \ \"{{ _extra_port.protocol | default('TCP') }}\"\n    port: {{ _extra_port.port\
  \ }}\n{% endfor %}\n{% endif %}\n- from:\n  - podSelector:\n      matchLabels:\n\
  \        {{ meta_app_connects_to }}/{{ php_fpm_appname }}: 'true'\n{% if php_fpm_netpol_ingress_ipblock\
  \ is defined and php_fpm_netpol_ingress_ipblock %}\n  - ipBlock:\n      cidr: '{{\
  \ php_fpm_netpol_ingress_ipblock }}'\n{% endif %}\negress:\n- ports:\n  - protocol:\
  \ TCP\n    port: 53\n  - protocol: UDP\n    port: 53\n  - protocol: TCP\n    port:\
  \ 80\n  - protocol: TCP\n    port: 443\n{% for _extra_port in php_fpm_netpol_egress_extra_ports\
  \ | default([]) %}\n  - protocol: \"{{ _extra_port.protocol | default('TCP') }}\"\
  \n    port: {{ _extra_port.port }}\n{% endfor %}\n{% for php_fpm_netpol_connects_to_app_name\
  \ in php_fpm_netpol_connects_to if php_fpm_netpol_connects_to_app_name %}\n- to:\n\
  \  - podSelector:\n      matchLabels:\n        app.kubernetes.io/name: '{{ php_fpm_netpol_connects_to_app_name\
  \ }}'\n  - namespaceSelector:\n      matchLabels:\n        app.kubernetes.io/name:\
  \ '{{ php_fpm_netpol_connects_to_app_name }}'\n    podSelector:\n      matchLabels:\n\
  \        app.kubernetes.io/name: '{{ php_fpm_netpol_connects_to_app_name }}'\n{%\
  \ endfor %}\n{% if php_fpm_netpol_egress_ipblock is defined and php_fpm_netpol_egress_ipblock\
  \ %}\n  - ipBlock:\n      cidr: '{{ php_fpm_netpol_egress_ipblock }}'\n{% endif\
  \ %}"

```
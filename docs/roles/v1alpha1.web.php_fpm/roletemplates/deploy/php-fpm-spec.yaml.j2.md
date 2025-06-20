



# php-fpm-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
{% if not (php_fpm_hpa_spec is defined and php_fpm_hpa_spec) or cr_state == 'suspended' %}
replicas: {{ 0 if cr_state == 'suspended' else php_fpm_size }}
{% endif %}
selector:
  matchLabels:
    app: '{{ php_fpm_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ php_fpm_term_grace_period }}
    automountServiceAccountToken: false
{% if php_fpm_init_containers is defined and php_fpm_init_containers %}
    initContainers:
    {{ php_fpm_init_containers | indent(4) }}
{% endif %}
    containers:
    - name: '{{ php_fpm_container }}'
      image: '{{ php_fpm_image }}'
      env:
      - name: PHP_FPM_LISTEN
        value: '9000'
      - name: PHP_FPM_LISTEN_ALLOWED_CLIENTS
        value: any
      - name: PHP_FPM_PROCESS_CONTROL_TIMEOUT
        value: '{{ php_fpm_config_process_control_timeout }}'
      - name: PHP_FPM_CHECK_SOCKET_TIMEOUT
        value: '{{ php_fpm_liveness_timeout - 0.2 }}'
{% if php_fpm_envvars is defined and php_fpm_envvars %}
{%   for php_fpm_envvar in php_fpm_envvars %}
      - name: {{ php_fpm_envvar.name }}
{%     if php_fpm_envvar.value is defined %}
        value: {{ php_fpm_envvar.value }}
{%     endif %}
{%     if php_fpm_envvar.source is defined %}
        valueFrom:
          {{ php_fpm_envvar.source | indent(10) }}
{%     endif %}
{%   endfor %}
{% endif %}
      ports:
      - containerPort: {{ php_fpm_port }}
      imagePullPolicy: {{ php_fpm_image_pull_policy | default('IfNotPresent') }}
{% if php_fpm_command is defined and php_fpm_command %}
{%   if php_fpm_command is string %}
      command: {{ php_fpm_command }}
{%   elif php_fpm_command | type_debug == 'list' %}
      command:
      {{ php_fpm_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if php_fpm_args is defined and php_fpm_args %}
{%   if php_fpm_args is string %}
      args: {{ php_fpm_args }}
{%   elif php_fpm_args | type_debug == 'list' %}
      args:
      {{ php_fpm_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if php_fpm_startup_probe %}
      startupProbe:
{%   if php_fpm_startup_command is defined and php_fpm_startup_command %}
        exec:
{%     if php_fpm_startup_command is string %}
          command: {{ php_fpm_startup_command }}
{%     elif php_fpm_startup_command | type_debug == 'list' %}
          command:
          {{ php_fpm_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif php_fpm_startup_path is defined and php_fpm_startup_path %}
        httpGet:
          path: '{{ php_fpm_startup_path }}'
          port: {{ php_fpm_startup_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ php_fpm_startup_host }}'
{%   endif %}
        initialDelaySeconds: {{ php_fpm_startup_initial }}
        periodSeconds: {{ php_fpm_startup_period }}
        timeoutSeconds: {{ php_fpm_startup_timeout }}
        successThreshold: {{ php_fpm_startup_success }}
        failureThreshold: {{ php_fpm_startup_failure }}
{% endif %}
{% if php_fpm_readiness_probe %}
      readinessProbe:
{%   if php_fpm_readiness_command is defined and php_fpm_readiness_command %}
        exec:
{%     if php_fpm_readiness_command is string %}
          command: {{ php_fpm_readiness_command }}
{%     elif php_fpm_readiness_command | type_debug == 'list' %}
          command:
          {{ php_fpm_readiness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif php_fpm_readiness_path is defined and php_fpm_readiness_path %}
        httpGet:
          path: '{{ php_fpm_readiness_path }}'
          port: {{ php_fpm_readiness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ php_fpm_readiness_host }}'
{%   endif %}
        initialDelaySeconds: {{ php_fpm_readiness_initial }}
        periodSeconds: {{ php_fpm_readiness_period }}
        timeoutSeconds: {{ php_fpm_readiness_timeout }}
        successThreshold: {{ php_fpm_readiness_success }}
        failureThreshold: {{ php_fpm_readiness_failure }}
{% endif %}
{% if php_fpm_liveness_probe %}
      livenessProbe:
{%   if php_fpm_liveness_command is defined and php_fpm_liveness_command %}
        exec:
{%     if php_fpm_liveness_command is string %}
          command: {{ php_fpm_liveness_command }}
{%     elif php_fpm_liveness_command | type_debug == 'list' %}
          command:
          {{ php_fpm_liveness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif php_fpm_liveness_path is defined and php_fpm_liveness_path %}
        httpGet:
          path: '{{ php_fpm_liveness_path }}'
          port: {{ php_fpm_liveness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ php_fpm_liveness_host }}'
{%   endif %}
        initialDelaySeconds: {{ php_fpm_liveness_initial }}
        periodSeconds: {{ php_fpm_liveness_period }}
        timeoutSeconds: {{ php_fpm_liveness_timeout }}
        successThreshold: {{ php_fpm_liveness_success }}
        failureThreshold: {{ php_fpm_liveness_failure }}
{% endif %}
{% if php_fpm_resource_requests or php_fpm_resource_limits %}
      resources:
{%   if php_fpm_resource_requests %}
        requests:
          cpu: '{{ php_fpm_resource_requests_cpu }}'
          memory: '{{ php_fpm_resource_requests_memory }}'
{%   endif %}
{%   if php_fpm_resource_limits %}
        limits:
          cpu: '{{ php_fpm_resource_limits_cpu }}'
          memory: '{{ php_fpm_resource_limits_memory }}'
{%   endif %}
{% endif %}
{% if (k8s_distribution == 'k8s' and php_fpm_run_as_user is defined and php_fpm_run_as_user) or php_fpm_security_context is defined %}
      securityContext:
{%   if k8s_distribution == 'k8s' and php_fpm_run_as_user is defined and php_fpm_run_as_user and php_fpm_security_context.runAsUser is not defined %}
        runAsUser: {{ php_fpm_run_as_user }}
{%   endif %}
{%   if php_fpm_security_context is defined %}
        {{ php_fpm_security_context | indent(8) }}
{%   endif %}
{% endif %}
      volumeMounts:
      - mountPath: /etc/php.d/99-php-extra.ini
        name: php-fpm-extra-config
        subPath: php-extra.ini
      - mountPath: /etc/php-fpm.d/zz-php-fpm-extra.conf
        name: php-fpm-extra-config
        subPath: php-fpm-extra.conf
{% if php_fpm_volumes is defined and php_fpm_volumes %}
{%   for volume in php_fpm_volumes %}
      - name: '{{ volume.name }}'
        mountPath: '{{ volume.mount_path }}'
{%     if volume.sub_path is defined and volume.sub_path %}
        subPath: {{ volume.sub_path }}
{%     endif %}
{%     if volume.sub_path_expr is defined and  volume.sub_path_expr %}
        subPathExpr: {{ volume.sub_path_expr }}
{%     endif %}
{%     if volume.read_only is defined and volume.read_only %}
        readOnly: true
{%     endif %}
{%   endfor %}
{% endif %}
    volumes:
    - name: php-fpm-extra-config
      configMap:
        name: '{{ php_fpm_cm }}'
        defaultMode: 0664
        items:
        - key: php-extra.ini
          path: php-extra.ini
        - key: php-fpm-extra.conf
          path: php-fpm-extra.conf
{% if php_fpm_volumes is defined and php_fpm_volumes %}
{%   for volume in php_fpm_volumes %}
{%     if volume.source is defined and volume.source %}
    - name: '{{ volume.name }}'
      {{ volume.source | indent(6) }}
{%     endif %}
{%   endfor %}
{% endif %}
{% if php_fpm_tolerations %}
    tolerations:
    {{ php_fpm_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if php_fpm_image_pull_secret %}
    imagePullSecrets:
    - name: {{ php_fpm_image_pull_secret }}
{% endif %}
{% if php_fpm_node_selector %}
    nodeSelector:
      {{ php_fpm_node_selector | indent(6) }}
{% endif %}
{% if php_fpm_affinity %}
    affinity:
      {{ php_fpm_affinity | indent(6) }}
{% endif %}

```
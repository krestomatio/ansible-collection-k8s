



# nginx-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
{% if not (nginx_hpa_spec is defined and nginx_hpa_spec) or cr_state == 'suspended' %}
replicas: {{ 0 if cr_state == 'suspended' else nginx_size }}
{% endif %}
selector:
  matchLabels:
    app: '{{ nginx_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ nginx_term_grace_period }}
    automountServiceAccountToken: false
{% if nginx_init_containers is defined and nginx_init_containers %}
    initContainers:
    {{ nginx_init_containers | indent(4) }}
{% endif %}
    containers:
    - name: '{{ nginx_container }}'
      image: '{{ nginx_image }}'
{% if nginx_envvars is defined and nginx_envvars %}
      env:
{%   for nginx_envvar in nginx_envvars %}
      - name: {{ nginx_envvar.name }}
{%     if nginx_envvar.value is defined %}
        value: {{ nginx_envvar.value }}
{%     endif %}
{%     if nginx_envvar.source is defined %}
        valueFrom:
          {{ nginx_envvar.source | indent(10) }}
{%     endif %}
{%   endfor %}
{% endif %}
      ports:
      - containerPort: {{ nginx_port }}
      imagePullPolicy: {{ nginx_image_pull_policy | default('IfNotPresent') }}
{% if nginx_command is defined and nginx_command %}
{%   if nginx_command is string %}
      command: {{ nginx_command }}
{%   elif nginx_command | type_debug == 'list' %}
      command:
      {{ nginx_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if nginx_args is defined and nginx_args %}
{%   if nginx_args is string %}
      args: {{ nginx_args }}
{%   elif nginx_args | type_debug == 'list' %}
      args:
      {{ nginx_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if nginx_startup_probe %}
      startupProbe:
{%   if nginx_startup_command is defined and nginx_startup_command %}
        exec:
{%     if nginx_startup_command is string %}
          command: {{ nginx_startup_command }}
{%     elif nginx_startup_command | type_debug == 'list' %}
          command:
          {{ nginx_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif nginx_startup_path is defined and nginx_startup_path %}
        httpGet:
          path: '{{ nginx_startup_path }}'
          port: {{ nginx_startup_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ nginx_startup_host }}'
{%   endif %}
        initialDelaySeconds: {{ nginx_startup_initial }}
        periodSeconds: {{ nginx_startup_period }}
        timeoutSeconds: {{ nginx_startup_timeout }}
        successThreshold: {{ nginx_startup_success }}
        failureThreshold: {{ nginx_startup_failure }}
{% endif %}
{% if nginx_readiness_probe %}
      readinessProbe:
{%   if nginx_readiness_command is defined and nginx_readiness_command %}
        exec:
{%     if nginx_readiness_command is string %}
          command: {{ nginx_readiness_command }}
{%     elif nginx_readiness_command | type_debug == 'list' %}
          command:
          {{ nginx_readiness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif nginx_readiness_path is defined and nginx_readiness_path %}
        httpGet:
          path: '{{ nginx_readiness_path }}'
          port: {{ nginx_readiness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ nginx_readiness_host }}'
{%   endif %}
        initialDelaySeconds: {{ nginx_readiness_initial }}
        periodSeconds: {{ nginx_readiness_period }}
        timeoutSeconds: {{ nginx_readiness_timeout }}
        successThreshold: {{ nginx_readiness_success }}
        failureThreshold: {{ nginx_readiness_failure }}
{% endif %}
{% if nginx_liveness_probe %}
      livenessProbe:
{%   if nginx_liveness_command is defined and nginx_liveness_command %}
        exec:
{%     if nginx_liveness_command is string %}
          command: {{ nginx_liveness_command }}
{%     elif nginx_liveness_command | type_debug == 'list' %}
          command:
          {{ nginx_liveness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif nginx_liveness_path is defined and nginx_liveness_path %}
        httpGet:
          path: '{{ nginx_liveness_path }}'
          port: {{ nginx_liveness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ nginx_liveness_host }}'
{%   endif %}
        initialDelaySeconds: {{ nginx_liveness_initial }}
        periodSeconds: {{ nginx_liveness_period }}
        timeoutSeconds: {{ nginx_liveness_timeout }}
        successThreshold: {{ nginx_liveness_success }}
        failureThreshold: {{ nginx_liveness_failure }}
{% endif %}
{% if nginx_resource_requests or nginx_resource_limits %}
      resources:
{%   if nginx_resource_requests %}
        requests:
          cpu: '{{ nginx_resource_requests_cpu }}'
          memory: '{{ nginx_resource_requests_memory }}'
{%   endif %}
{%   if nginx_resource_limits %}
        limits:
          cpu: '{{ nginx_resource_limits_cpu }}'
          memory: '{{ nginx_resource_limits_memory }}'
{%   endif %}
{% endif %}
{% if (k8s_distribution == 'k8s' and nginx_run_as_user is defined and nginx_run_as_user) or nginx_security_context is defined %}
      securityContext:
{%   if k8s_distribution == 'k8s' and nginx_run_as_user is defined and nginx_run_as_user and nginx_security_context.runAsUser is not defined %}
        runAsUser: {{ nginx_run_as_user }}
{%   endif %}
{%   if nginx_security_context is defined %}
        {{ nginx_security_context | indent(8) }}
{%   endif %}
{% endif %}
      volumeMounts:
      - mountPath: /etc/nginx/default.d/zz-nginx-extra.conf
        name: nginx-extra-config
        subPath: nginx-extra.conf
{% if nginx_volumes is defined and nginx_volumes %}
{%   for volume in nginx_volumes %}
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
    - name: nginx-extra-config
      configMap:
        name: '{{ nginx_cm }}'
        defaultMode: 0664
        items:
        - key: nginx-extra.conf
          path: nginx-extra.conf
{% if nginx_volumes is defined and nginx_volumes %}
{%   for volume in nginx_volumes %}
{%     if volume.source is defined and volume.source %}
    - name: '{{ volume.name }}'
      {{ volume.source | indent(6) }}
{%     endif %}
{%   endfor %}
{% endif %}
{% if nginx_tolerations %}
    tolerations:
    {{ nginx_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if nginx_image_pull_secret %}
    imagePullSecrets:
    - name: {{ nginx_image_pull_secret }}
{% endif %}
{% if nginx_node_selector %}
    nodeSelector:
      {{ nginx_node_selector | indent(6) }}
{% endif %}
{% if nginx_affinity %}
    affinity:
      {{ nginx_affinity | indent(6) }}
{% endif %}

```




# keydb-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
replicas: {{ 0 if cr_state == 'suspended' else keydb_size }}
serviceName: '{{ keydb_service_headless }}'
selector:
  matchLabels:
    app: '{{ keydb_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ keydb_term_grace_period }}
    automountServiceAccountToken: false
{% if keydb_sysctls is defined and keydb_sysctls %}
    securityContext:
      sysctls:
      {{ keydb_sysctls | to_nice_yaml(indent=2) | indent(6) }}
{% endif %}
{% if k8s_distribution == 'k8s' and keydb_pvc_enabled | bool %}
    initContainers:
    - name: 'data-dir-permissions'
      image: '{{ keydb_image }}'
      securityContext:
        runAsUser: 0
      command:
        - '/bin/bash'
        - '-c'
        - |
          chown ${CTR_USER_ID}:${CTR_GROUP_ID:-0} '{{ keydb_data }}'
          chmod 0700 '{{ keydb_data }}'
      volumeMounts:
      - mountPath: '{{ keydb_data }}'
        name: {{ keydb_pvc_data }}
{% endif %}
    containers:
    - name: '{{ keydb_container }}'
      image: '{{ keydb_image }}'
      imagePullPolicy: '{{ keydb_image_pull_policy | default('IfNotPresent') }}'
      env:
      - name: KEYDB_MODE
        value: '{{ keydb_mode }}'
      - name: KEYDB_PORT
        value: '{{ keydb_port }}'
      - name: KEYDB_PASSWORD
        valueFrom:
          secretKeyRef:
            name: '{{ keydb_secret }}'
            key: keydb_password
      - name: KEYDB_DATA
        value: '{{ keydb_data }}'
      - name: KEYDB_REPLICA_NUMBER
        value: '{{ keydb_size }}'
      - name: KEYDB_REPLICA_BASE_NAME
        value: '{{ keydb_sts }}'
      - name: KEYDB_REPLICA_BASE_DOMAIN
        value: '{{ keydb_service_headless }}'
      ports:
      - containerPort: {{ keydb_port }}
        name: keydb
{% if keydb_command is defined and keydb_command %}
{%   if keydb_command is string %}
      command: {{ keydb_command }}
{%   elif keydb_command | type_debug == 'list' %}
      command:
      {{ keydb_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if keydb_args is defined and keydb_args %}
{%   if keydb_args is string %}
      args: {{ keydb_args }}
{%   elif keydb_args | type_debug == 'list' %}
      args:
      {{ keydb_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if keydb_startup_probe | bool %}
      startupProbe:
        exec:
{%   if keydb_startup_command is string %}
          command: {{ keydb_startup_command }}
{%   elif keydb_startup_command | type_debug == 'list' %}
          command:
          {{ keydb_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%   endif %}
        initialDelaySeconds: {{ keydb_startup_initial }}
        periodSeconds: {{ keydb_startup_period }}
        timeoutSeconds: {{ keydb_startup_timeout }}
        successThreshold: {{ keydb_startup_success }}
        failureThreshold: {{ keydb_startup_failure }}
{% endif %}
{% if keydb_readiness_probe | bool %}
      readinessProbe:
        exec:
{%   if keydb_readiness_command is string %}
          command: {{ keydb_readiness_command }}
{%   elif keydb_readiness_command | type_debug == 'list' %}
          command:
          {{ keydb_readiness_command | to_nice_yaml(indent=2) | indent(10) }}
{%   endif %}
        initialDelaySeconds: {{ keydb_readiness_initial }}
        periodSeconds: {{ keydb_readiness_period }}
        timeoutSeconds: {{ keydb_readiness_timeout }}
        successThreshold: {{ keydb_readiness_success }}
        failureThreshold: {{ keydb_readiness_failure }}
{% endif %}
{% if keydb_liveness_probe | bool %}
      livenessProbe:
        exec:
{%   if keydb_liveness_command is string %}
          command: {{ keydb_liveness_command }}
{%   elif keydb_liveness_command | type_debug == 'list' %}
          command:
          {{ keydb_liveness_command | to_nice_yaml(indent=2) | indent(10) }}
{%   endif %}
        initialDelaySeconds: {{ keydb_liveness_initial }}
        periodSeconds: {{ keydb_liveness_period }}
        timeoutSeconds: {{ keydb_liveness_timeout }}
        successThreshold: {{ keydb_liveness_success }}
        failureThreshold: {{ keydb_liveness_failure }}
{% endif %}
{% if keydb_resource_requests | bool or keydb_resource_limits | bool %}
      resources:
{%   if keydb_resource_requests | bool %}
        requests:
          cpu: '{{ keydb_resource_requests_cpu }}'
          memory: '{{ keydb_resource_requests_memory }}'
{%   endif %}
{%   if keydb_resource_limits | bool %}
        limits:
          cpu: '{{ keydb_resource_limits_cpu }}'
          memory: '{{ keydb_resource_limits_memory }}'
{%   endif %}
{% endif %}
      volumeMounts:
      - mountPath: /etc/keydb/keydb.conf
        name: keydb-config
        subPath: keydb.conf
{% if keydb_pvc_enabled | bool %}
      - mountPath: '{{ keydb_data }}'
        name: {{ keydb_pvc_data }}
{% else %}
      - mountPath: '{{ keydb_data }}'
        name: keydb-data
{% endif %}
    volumes:
    - name: keydb-config
      configMap:
        name: '{{ keydb_cm }}'
        defaultMode: 0644
        items:
        - key: keydb.conf
          path: keydb.conf
{% if not keydb_pvc_enabled | bool %}
    - name: keydb-data
      emptyDir:
        {{ keydb_empty_dir_data | indent(8) }}
{% endif %}
{% if keydb_tolerations is defined and keydb_tolerations %}
    tolerations:
    {{ keydb_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if keydb_image_pull_secret is defined and keydb_image_pull_secret %}
    imagePullSecrets:
    - name: {{ keydb_image_pull_secret }}
{% endif %}
{% if keydb_node_selector %}
    nodeSelector:
      {{ keydb_node_selector | indent(6) }}
{% endif %}
{% if keydb_affinity %}
    affinity:
      {{ keydb_affinity | indent(6) }}
{% endif %}
{% if keydb_pvc_enabled | bool %}
volumeClaimTemplates:
  {{ keydb_volume_claim_template | to_nice_yaml(indent=2) | indent(2) }}
{% endif %}

```
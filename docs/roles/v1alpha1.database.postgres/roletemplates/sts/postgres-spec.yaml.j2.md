



# postgres-spec.yaml.j2
  
---  
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
replicas: {{ 0 if cr_state == 'suspended' else 1 }}
serviceName: '{{ postgres_service }}'
selector:
  matchLabels:
    app: '{{ postgres_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ postgres_term_grace_period }}
    automountServiceAccountToken: false
{% if postgres_sysctls is defined and postgres_sysctls %}
    securityContext:
      sysctls:
      {{ postgres_sysctls | to_nice_yaml(indent=2) | indent(6) }}
{% endif %}
{% if k8s_distribution == 'k8s' %}
    initContainers:
    - name: 'data-dir-permissions'
      image: '{{ postgres_image }}'
      securityContext:
        runAsUser: 0
      command:
        - '/bin/bash'
        - '-c'
        - |
          chown ${CTR_USER_ID}:${CTR_GROUP_ID:-0} '{{ postgres_data }}'
          chmod 0700 '{{ postgres_data }}'
      volumeMounts:
      - mountPath: '{{ postgres_data }}'
        name: {{ postgres_pvc_data }}
{% endif %}
    containers:
    - name: '{{ postgres_container }}'
      image: '{{ postgres_image }}'
      imagePullPolicy: '{{ postgres_image_pull_policy | default('IfNotPresent') }}'
      env:
      - name: APP_DATA
        value: /var/lib/pgsql
      - name: ENABLE_REPLICATION
        value: "{{ 'true' if postgres_mode in ['readreplicas'] else 'false' }}"
{% if postgres_upgrade %}
      - name: POSTGRESQL_UPGRADE
        value: "copy"
{% endif %}
{% if postgres_config_log_stderr %}
      - name: POSTGRESQL_LOG_STDERR
        value: "true"
{% endif %}
      - name: POSTGRESQL_MASTER_USER
        valueFrom:
          secretKeyRef:
            name: '{{ postgres_secret }}'
            key: database_master_user
      - name: POSTGRESQL_MASTER_PASSWORD
        valueFrom:
          secretKeyRef:
            name: '{{ postgres_secret }}'
            key: database_master_password
      - name: POSTGRESQL_DATABASE
        valueFrom:
          secretKeyRef:
            name: '{{ postgres_secret }}'
            key: database_name
      - name: POSTGRESQL_USER
        valueFrom:
          secretKeyRef:
            name: '{{ postgres_secret }}'
            key: database_user
      - name: POSTGRESQL_PASSWORD
        valueFrom:
          secretKeyRef:
            name: '{{ postgres_secret }}'
            key: database_password
      envFrom:
      - configMapRef:
          name: {{ postgres_cm_vars }}
      ports:
      - containerPort: {{ postgres_port }}
        name: postgres
{% if postgres_command is defined and postgres_command %}
{%   if postgres_command is string %}
      command: {{ postgres_command }}
{%   elif postgres_command | type_debug == 'list' %}
      command:
      {{ postgres_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if postgres_args is defined and postgres_args %}
{%   if postgres_args is string %}
      args: {{ postgres_args }}
{%   elif postgres_args | type_debug == 'list' %}
      args:
      {{ postgres_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if postgres_startup_probe %}
      startupProbe:
{%   if postgres_startup_command is defined and postgres_startup_command %}
        exec:
{%     if postgres_startup_command is string %}
          command: {{ postgres_startup_command }}
{%     elif postgres_startup_command | type_debug == 'list' %}
          command:
          {{ postgres_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif postgres_startup_path is defined and postgres_startup_path %}
        httpGet:
          path: '{{ postgres_startup_path }}'
          port: {{ postgres_startup_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ postgres_startup_host }}'
{%   endif %}
        initialDelaySeconds: {{ postgres_startup_initial }}
        periodSeconds: {{ postgres_startup_period }}
        timeoutSeconds: {{ postgres_startup_timeout }}
        successThreshold: {{ postgres_startup_success }}
        failureThreshold: {{ postgres_startup_failure }}
{% endif %}
{% if postgres_readiness_probe %}
      readinessProbe:
{%   if postgres_readiness_command is defined and postgres_readiness_command %}
        exec:
{%     if postgres_readiness_command is string %}
          command: {{ postgres_readiness_command }}
{%     elif postgres_readiness_command | type_debug == 'list' %}
          command:
          {{ postgres_readiness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif postgres_readiness_path is defined and postgres_readiness_path %}
        httpGet:
          path: '{{ postgres_readiness_path }}'
          port: {{ postgres_readiness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ postgres_readiness_host }}'
{%   endif %}
        initialDelaySeconds: {{ postgres_readiness_initial }}
        periodSeconds: {{ postgres_readiness_period }}
        timeoutSeconds: {{ postgres_readiness_timeout }}
        successThreshold: {{ postgres_readiness_success }}
        failureThreshold: {{ postgres_readiness_failure }}
{% endif %}
{% if postgres_liveness_probe %}
      livenessProbe:
{%   if postgres_liveness_command is defined and postgres_liveness_command %}
        exec:
{%     if postgres_liveness_command is string %}
          command: {{ postgres_liveness_command }}
{%     elif postgres_liveness_command | type_debug == 'list' %}
          command:
          {{ postgres_liveness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif postgres_liveness_path is defined and postgres_liveness_path %}
        httpGet:
          path: '{{ postgres_liveness_path }}'
          port: {{ postgres_liveness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ postgres_liveness_host }}'
{%   endif %}
        initialDelaySeconds: {{ postgres_liveness_initial }}
        periodSeconds: {{ postgres_liveness_period }}
        timeoutSeconds: {{ postgres_liveness_timeout }}
        successThreshold: {{ postgres_liveness_success }}
        failureThreshold: {{ postgres_liveness_failure }}
{% endif %}
{% if postgres_resource_requests | bool or postgres_resource_limits | bool %}
      resources:
{%   if postgres_resource_requests | bool %}
        requests:
          cpu: '{{ postgres_resource_requests_cpu }}'
          memory: '{{ postgres_resource_requests_memory }}'
{%   endif %}
{%   if postgres_resource_limits | bool %}
        limits:
          cpu: '{{ postgres_resource_limits_cpu }}'
          memory: '{{ postgres_resource_limits_memory }}'
{%   endif %}
{% endif %}
      volumeMounts:
      - mountPath: /var/lib/pgsql/src/postgresql-cfg/postgres-extra.conf
        name: postgres-extra-config
        subPath: postgres-extra.conf
      - mountPath: '{{ postgres_data }}'
        name: {{ postgres_pvc_data }}
    volumes:
    - name: postgres-extra-config
      configMap:
        name: '{{ postgres_cm }}'
        defaultMode: 0644
        items:
        - key: postgres-extra.conf
          path: postgres-extra.conf
{% if postgres_tolerations is defined and postgres_tolerations %}
    tolerations:
    {{ postgres_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if postgres_image_pull_secret is defined and postgres_image_pull_secret %}
    imagePullSecrets:
    - name: {{ postgres_image_pull_secret }}
{% endif %}
{% if postgres_node_selector %}
    nodeSelector:
      {{ postgres_node_selector | indent(6) }}
{% endif %}
{% if postgres_affinity %}
    affinity:
      {{ postgres_affinity | indent(6) }}
{% endif %}
volumeClaimTemplates:
  {{ postgres_volume_claim_template | to_nice_yaml(indent=2) | indent(2) }}
  
```
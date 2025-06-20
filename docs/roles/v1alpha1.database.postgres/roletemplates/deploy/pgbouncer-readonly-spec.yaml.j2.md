



# pgbouncer-readonly-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
replicas: {{ 0 if cr_state == 'suspended' else 1 }}
selector:
  matchLabels:
    app: '{{ pgbouncer_readonly_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ pgbouncer_readonly_term_grace_period }}
    automountServiceAccountToken: false
{% if pgbouncer_readonly_sysctls is defined and pgbouncer_readonly_sysctls %}
    securityContext:
      sysctls:
      {{ pgbouncer_readonly_sysctls | to_nice_yaml(indent=2) | indent(6) }}
{% endif %}
    containers:
    - name: '{{ pgbouncer_readonly_container }}'
      image: '{{ pgbouncer_image }}'
      env:
        - name: PGBOUNCER_PORT
          value: "{{ pgbouncer_port }}"
        - name: POSTGRESQL_HOST
          value: "{{ postgres_readonly_service }}"
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
      ports:
      - containerPort: {{ pgbouncer_port }}
        name: pgbouncer
      imagePullPolicy: '{{ pgbouncer_readonly_image_pull_policy | default('IfNotPresent') }}'
{% if pgbouncer_readonly_command is defined and pgbouncer_readonly_command %}
{%   if pgbouncer_readonly_command is string %}
      command: {{ pgbouncer_readonly_command }}
{%   elif pgbouncer_readonly_command | type_debug == 'list' %}
      command:
      {{ pgbouncer_readonly_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if pgbouncer_readonly_args is defined and pgbouncer_readonly_args %}
{%   if pgbouncer_readonly_args is string %}
      args: {{ pgbouncer_readonly_args }}
{%   elif pgbouncer_readonly_args | type_debug == 'list' %}
      args:
      {{ pgbouncer_readonly_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if pgbouncer_readonly_startup_probe %}
      startupProbe:
{%   if pgbouncer_readonly_startup_command is defined and pgbouncer_readonly_startup_command %}
        exec:
{%     if pgbouncer_readonly_startup_command is string %}
          command: {{ pgbouncer_readonly_startup_command }}
{%     elif pgbouncer_readonly_startup_command | type_debug == 'list' %}
          command:
          {{ pgbouncer_readonly_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif pgbouncer_readonly_startup_path is defined and pgbouncer_readonly_startup_path %}
        httpGet:
          path: '{{ pgbouncer_readonly_startup_path }}'
          port: {{ pgbouncer_readonly_startup_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ pgbouncer_readonly_startup_host }}'
{%   endif %}
        initialDelaySeconds: {{ pgbouncer_readonly_startup_initial }}
        periodSeconds: {{ pgbouncer_readonly_startup_period }}
        timeoutSeconds: {{ pgbouncer_readonly_startup_timeout }}
        successThreshold: {{ pgbouncer_readonly_startup_success }}
        failureThreshold: {{ pgbouncer_readonly_startup_failure }}
{% endif %}
{% if pgbouncer_readonly_readiness_probe %}
      readinessProbe:
{%   if pgbouncer_readonly_readiness_command is defined and pgbouncer_readonly_readiness_command %}
        exec:
{%     if pgbouncer_readonly_readiness_command is string %}
          command: {{ pgbouncer_readonly_readiness_command }}
{%     elif pgbouncer_readonly_readiness_command | type_debug == 'list' %}
          command:
          {{ pgbouncer_readonly_readiness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif pgbouncer_readonly_readiness_path is defined and pgbouncer_readonly_readiness_path %}
        httpGet:
          path: '{{ pgbouncer_readonly_readiness_path }}'
          port: {{ pgbouncer_readonly_readiness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ pgbouncer_readonly_readiness_host }}'
{%   endif %}
        initialDelaySeconds: {{ pgbouncer_readonly_readiness_initial }}
        periodSeconds: {{ pgbouncer_readonly_readiness_period }}
        timeoutSeconds: {{ pgbouncer_readonly_readiness_timeout }}
        successThreshold: {{ pgbouncer_readonly_readiness_success }}
        failureThreshold: {{ pgbouncer_readonly_readiness_failure }}
{% endif %}
{% if pgbouncer_readonly_liveness_probe %}
      livenessProbe:
{%   if pgbouncer_readonly_liveness_command is defined and pgbouncer_readonly_liveness_command %}
        exec:
{%     if pgbouncer_readonly_liveness_command is string %}
          command: {{ pgbouncer_readonly_liveness_command }}
{%     elif pgbouncer_readonly_liveness_command | type_debug == 'list' %}
          command:
          {{ pgbouncer_readonly_liveness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif pgbouncer_readonly_liveness_path is defined and pgbouncer_readonly_liveness_path %}
        httpGet:
          path: '{{ pgbouncer_readonly_liveness_path }}'
          port: {{ pgbouncer_readonly_liveness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ pgbouncer_readonly_liveness_host }}'
{%   endif %}
        initialDelaySeconds: {{ pgbouncer_readonly_liveness_initial }}
        periodSeconds: {{ pgbouncer_readonly_liveness_period }}
        timeoutSeconds: {{ pgbouncer_readonly_liveness_timeout }}
        successThreshold: {{ pgbouncer_readonly_liveness_success }}
        failureThreshold: {{ pgbouncer_readonly_liveness_failure }}
{% endif %}
{% if pgbouncer_readonly_resource_requests or pgbouncer_readonly_resource_limits %}
      resources:
{%   if pgbouncer_readonly_resource_requests %}
        requests:
          cpu: '{{ pgbouncer_readonly_resource_requests_cpu }}'
          memory: '{{ pgbouncer_readonly_resource_requests_memory }}'
{%   endif %}
{%   if pgbouncer_readonly_resource_limits %}
        limits:
          cpu: '{{ pgbouncer_readonly_resource_limits_cpu }}'
          memory: '{{ pgbouncer_readonly_resource_limits_memory }}'
{%   endif %}
{% endif %}
      volumeMounts:
      - mountPath: /etc/pgbouncer/pgbouncer-extra.ini
        name: pgbouncer-extra-config
        subPath: pgbouncer-extra.ini
      - mountPath: /etc/pgbouncer/pgbouncer-extra-users.ini
        name: pgbouncer-extra-config
        subPath: pgbouncer-extra-users.ini
      - mountPath: /etc/pgbouncer/pgbouncer-extra-databases.ini
        name: pgbouncer-extra-config
        subPath: pgbouncer-extra-databases.ini
    volumes:
    - name: pgbouncer-extra-config
      configMap:
        name: '{{ pgbouncer_readonly_cm }}'
        defaultMode: 0664
        items:
        - key: pgbouncer-extra.ini
          path: pgbouncer-extra.ini
        - key: pgbouncer-extra-users.ini
          path: pgbouncer-extra-users.ini
        - key: pgbouncer-extra-databases.ini
          path: pgbouncer-extra-databases.ini
{% if pgbouncer_readonly_tolerations %}
    tolerations:
    {{ pgbouncer_readonly_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if pgbouncer_image_pull_secret %}
    imagePullSecrets:
    - name: {{ pgbouncer_image_pull_secret }}
{% endif %}
{% if pgbouncer_readonly_node_selector %}
    nodeSelector:
      {{ pgbouncer_readonly_node_selector | indent(6) }}
{% endif %}
{% if pgbouncer_readonly_affinity %}
    affinity:
      {{ pgbouncer_readonly_affinity | indent(6) }}
{% endif %}

```
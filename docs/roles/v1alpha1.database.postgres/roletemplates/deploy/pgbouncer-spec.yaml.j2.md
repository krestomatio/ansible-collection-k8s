



# pgbouncer-spec.yaml.j2
  
---  
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
replicas: {{ 0 if cr_state == 'suspended' else 1 }}
selector:
  matchLabels:
    app: '{{ pgbouncer_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ pgbouncer_term_grace_period }}
    automountServiceAccountToken: false
{% if pgbouncer_sysctls is defined and pgbouncer_sysctls %}
    securityContext:
      sysctls:
      {{ pgbouncer_sysctls | to_nice_yaml(indent=2) | indent(6) }}
{% endif %}
    containers:
    - name: '{{ pgbouncer_container }}'
      image: '{{ pgbouncer_image }}'
      env:
        - name: PGBOUNCER_PORT
          value: "{{ pgbouncer_port }}"
        - name: POSTGRESQL_HOST
          value: "{{ postgres_service }}"
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
      imagePullPolicy: '{{ pgbouncer_image_pull_policy | default('IfNotPresent') }}'
{% if pgbouncer_command is defined and pgbouncer_command %}
{%   if pgbouncer_command is string %}
      command: {{ pgbouncer_command }}
{%   elif pgbouncer_command | type_debug == 'list' %}
      command:
      {{ pgbouncer_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if pgbouncer_args is defined and pgbouncer_args %}
{%   if pgbouncer_args is string %}
      args: {{ pgbouncer_args }}
{%   elif pgbouncer_args | type_debug == 'list' %}
      args:
      {{ pgbouncer_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if pgbouncer_startup_probe %}
      startupProbe:
{%   if pgbouncer_startup_command is defined and pgbouncer_startup_command %}
        exec:
{%     if pgbouncer_startup_command is string %}
          command: {{ pgbouncer_startup_command }}
{%     elif pgbouncer_startup_command | type_debug == 'list' %}
          command:
          {{ pgbouncer_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif pgbouncer_startup_path is defined and pgbouncer_startup_path %}
        httpGet:
          path: '{{ pgbouncer_startup_path }}'
          port: {{ pgbouncer_startup_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ pgbouncer_startup_host }}'
{%   endif %}
        initialDelaySeconds: {{ pgbouncer_startup_initial }}
        periodSeconds: {{ pgbouncer_startup_period }}
        timeoutSeconds: {{ pgbouncer_startup_timeout }}
        successThreshold: {{ pgbouncer_startup_success }}
        failureThreshold: {{ pgbouncer_startup_failure }}
{% endif %}
{% if pgbouncer_readiness_probe %}
      readinessProbe:
{%   if pgbouncer_readiness_command is defined and pgbouncer_readiness_command %}
        exec:
{%     if pgbouncer_readiness_command is string %}
          command: {{ pgbouncer_readiness_command }}
{%     elif pgbouncer_readiness_command | type_debug == 'list' %}
          command:
          {{ pgbouncer_readiness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif pgbouncer_readiness_path is defined and pgbouncer_readiness_path %}
        httpGet:
          path: '{{ pgbouncer_readiness_path }}'
          port: {{ pgbouncer_readiness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ pgbouncer_readiness_host }}'
{%   endif %}
        initialDelaySeconds: {{ pgbouncer_readiness_initial }}
        periodSeconds: {{ pgbouncer_readiness_period }}
        timeoutSeconds: {{ pgbouncer_readiness_timeout }}
        successThreshold: {{ pgbouncer_readiness_success }}
        failureThreshold: {{ pgbouncer_readiness_failure }}
{% endif %}
{% if pgbouncer_liveness_probe %}
      livenessProbe:
{%   if pgbouncer_liveness_command is defined and pgbouncer_liveness_command %}
        exec:
{%     if pgbouncer_liveness_command is string %}
          command: {{ pgbouncer_liveness_command }}
{%     elif pgbouncer_liveness_command | type_debug == 'list' %}
          command:
          {{ pgbouncer_liveness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif pgbouncer_liveness_path is defined and pgbouncer_liveness_path %}
        httpGet:
          path: '{{ pgbouncer_liveness_path }}'
          port: {{ pgbouncer_liveness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ pgbouncer_liveness_host }}'
{%   endif %}
        initialDelaySeconds: {{ pgbouncer_liveness_initial }}
        periodSeconds: {{ pgbouncer_liveness_period }}
        timeoutSeconds: {{ pgbouncer_liveness_timeout }}
        successThreshold: {{ pgbouncer_liveness_success }}
        failureThreshold: {{ pgbouncer_liveness_failure }}
{% endif %}
{% if pgbouncer_resource_requests or pgbouncer_resource_limits %}
      resources:
{%   if pgbouncer_resource_requests %}
        requests:
          cpu: '{{ pgbouncer_resource_requests_cpu }}'
          memory: '{{ pgbouncer_resource_requests_memory }}'
{%   endif %}
{%   if pgbouncer_resource_limits %}
        limits:
          cpu: '{{ pgbouncer_resource_limits_cpu }}'
          memory: '{{ pgbouncer_resource_limits_memory }}'
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
        name: '{{ pgbouncer_cm }}'
        defaultMode: 0664
        items:
        - key: pgbouncer-extra.ini
          path: pgbouncer-extra.ini
        - key: pgbouncer-extra-users.ini
          path: pgbouncer-extra-users.ini
        - key: pgbouncer-extra-databases.ini
          path: pgbouncer-extra-databases.ini
{% if pgbouncer_tolerations %}
    tolerations:
    {{ pgbouncer_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if pgbouncer_image_pull_secret %}
    imagePullSecrets:
    - name: {{ pgbouncer_image_pull_secret }}
{% endif %}
{% if pgbouncer_node_selector %}
    nodeSelector:
      {{ pgbouncer_node_selector | indent(6) }}
{% endif %}
{% if pgbouncer_affinity %}
    affinity:
      {{ pgbouncer_affinity | indent(6) }}
{% endif %}
  
```
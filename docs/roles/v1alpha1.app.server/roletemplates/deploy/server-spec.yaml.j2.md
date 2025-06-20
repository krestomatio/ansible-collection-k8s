



# server-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
replicas: {{ server_size }}
selector:
  matchLabels:
    app: '{{ server_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ server_term_grace_period }}
    automountServiceAccountToken: {{ server_automount_service_account_token }}
    containers:
    - name: '{{ server_container }}'
      image: '{{ server_image }}'
      env:
{% if server_secret_handler is defined and server_secret_handler %}
      - name: {{ graphql_engine_secret_handler_key | upper }}
        valueFrom:
          secretKeyRef:
            name: '{{ graphql_engine_secret_handler }}'
            key: {{ graphql_engine_secret_handler_key }}
{% endif %}
{% if server_database_secret is defined and server_database_secret %}
{%   for db_key in [server_database_secret_dbname_key,
                      server_database_secret_dbuser_key,
                      server_database_secret_dbpass_key,
                      server_database_secret_dburl_key] %}
      - name: {{ db_key | upper }}
        valueFrom:
          secretKeyRef:
            name: '{{ server_database_secret }}'
            key: {{ db_key }}
{%   endfor %}
{% endif %}
{% if server_envvars is defined and server_envvars %}
      {{ server_envvars | to_nice_yaml(indent=2) | indent(6) }}
{% endif %}
{% if server_secret_envfrom is defined and server_secret_envfrom %}
      envFrom:
{%   for secret_ref in server_secret_envfrom %}
      - secretRef:
          name: {{ secret_ref }}
{%   endfor %}
{% endif %}
      ports:
      - containerPort: {{ server_port }}
      imagePullPolicy: IfNotPresent
{% if server_command is defined and server_command %}
{%   if server_command is string %}
      command: {{ server_command }}
{%   elif server_command | type_debug == 'list' %}
      command:
      {{ server_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if server_args is defined and server_args %}
{%   if server_args is string %}
      # one
      args: {{ server_args }}
{%   elif server_args | type_debug == 'list' %}
      # two
      args:
      {{ server_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if server_readiness_probe %}
      readinessProbe:
        httpGet:
          path: '{{ server_readiness_path }}'
          port: {{ server_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ server_host }}'
        initialDelaySeconds: {{ server_readiness_initial }}
        periodSeconds: {{ server_readiness_period }}
        timeoutSeconds: {{ server_readiness_timeout }}
        successThreshold: {{ server_readiness_success }}
        failureThreshold: {{ server_readiness_failure }}
{% endif %}
{% if server_liveness_probe %}
      livenessProbe:
        httpGet:
          path: '{{ server_liveness_path }}'
          port: {{ server_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ server_host }}'
        initialDelaySeconds: {{ server_liveness_initial }}
        periodSeconds: {{ server_liveness_period }}
        timeoutSeconds: {{ server_liveness_timeout }}
        successThreshold: {{ server_liveness_success }}
        failureThreshold: {{ server_liveness_failure }}
{% endif %}
{% if server_resource_requests or server_resource_limits %}
      resources:
{% if server_resource_requests %}
        requests:
          cpu: '{{ server_resource_requests_cpu }}'
          memory: '{{ server_resource_requests_memory }}'
{% endif %}
{% if server_resource_limits %}
        limits:
          cpu: '{{ server_resource_limits_cpu }}'
          memory: '{{ server_resource_limits_memory }}'
{% endif %}
{% endif %}
{% if k8s_distribution == 'k8s' %}
      securityContext:
        runAsUser: {{ server_run_as_user }}
{% endif %}
{% if server_volumes is defined and server_volumes %}
      volumeMounts:
{%   for volume in server_volumes %}
      - name: '{{ volume.name }}'
        mountPath: '{{ volume.mount_path }}'
{%     if volume.read_only is defined and volume.read_only %}
        readOnly: true
{%     endif %}
{%   endfor %}
{% endif %}
{% if server_volumes is defined and server_volumes %}
    volumes:
{%   for volume in server_volumes %}
{%     if volume.source is defined and volume.source %}
    - name: '{{ volume.name }}'
      {{ volume.source | to_nice_yaml(indent=2) | indent(6) }}
{%     endif %}
{%   endfor %}
{% endif %}
{% if server_tolerations %}
    tolerations:
    {{ server_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if server_image_pull_secret %}
    imagePullSecrets:
    - name: {{ server_image_pull_secret }}
{% endif %}

```
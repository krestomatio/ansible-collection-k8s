



# graphql-engine-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
replicas: {{ graphql_engine_size }}
selector:
  matchLabels:
    app: '{{ graphql_engine_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ graphql_engine_term_grace_period }}
    automountServiceAccountToken: false
    containers:
    - name: '{{ graphql_engine_container }}'
      image: '{{ graphql_engine_image }}'
      env:
      - name: {{ graphql_engine_secret_handler_key | upper }}
        valueFrom:
          secretKeyRef:
            name: '{{ graphql_engine_secret_handler }}'
            key: {{ graphql_engine_secret_handler_key }}
{% if graphql_engine_database_secret is defined and graphql_engine_database_secret %}
      - name: HASURA_GRAPHQL_DATABASE_URL
        valueFrom:
          secretKeyRef:
            name: '{{ graphql_engine_database_secret }}'
            key: {{ graphql_engine_database_secret_dburl_key }}
{% endif %}
{% if graphql_engine_envvars is defined and graphql_engine_envvars %}
      {{ graphql_engine_envvars | to_nice_yaml(indent=2) | indent(6) }}
{% endif %}
{% if graphql_engine_secret_envfrom is defined and graphql_engine_secret_envfrom %}
      envFrom:
{%   for secret_ref in graphql_engine_secret_envfrom %}
      - secretRef:
          name: {{ secret_ref }}
{%   endfor %}
{% endif %}
      ports:
      - containerPort: {{ graphql_engine_port }}
      imagePullPolicy: IfNotPresent
{% if graphql_engine_args is defined and graphql_engine_args %}
{%   if graphql_engine_args is string %}
      args: {{ graphql_engine_args }}
{%   elif graphql_engine_args | type_debug == 'list' %}
      args:
      {{ graphql_engine_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if graphql_engine_readiness_probe %}
      readinessProbe:
        httpGet:
          path: '{{ graphql_engine_readiness_path }}'
          port: {{ graphql_engine_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ graphql_engine_host }}'
        initialDelaySeconds: {{ graphql_engine_readiness_initial }}
        periodSeconds: {{ graphql_engine_readiness_period }}
        timeoutSeconds: {{ graphql_engine_readiness_timeout }}
        successThreshold: {{ graphql_engine_readiness_success }}
        failureThreshold: {{ graphql_engine_readiness_failure }}
{% endif %}
{% if graphql_engine_liveness_probe %}
      livenessProbe:
        httpGet:
          path: '{{ graphql_engine_liveness_path }}'
          port: {{ graphql_engine_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ graphql_engine_host }}'
        initialDelaySeconds: {{ graphql_engine_liveness_initial }}
        periodSeconds: {{ graphql_engine_liveness_period }}
        timeoutSeconds: {{ graphql_engine_liveness_timeout }}
        successThreshold: {{ graphql_engine_liveness_success }}
        failureThreshold: {{ graphql_engine_liveness_failure }}
{% endif %}
{% if graphql_engine_resource_requests or graphql_engine_resource_limits %}
      resources:
{% if graphql_engine_resource_requests %}
        requests:
          cpu: '{{ graphql_engine_resource_requests_cpu }}'
          memory: '{{ graphql_engine_resource_requests_memory }}'
{% endif %}
{% if graphql_engine_resource_limits %}
        limits:
          cpu: '{{ graphql_engine_resource_limits_cpu }}'
          memory: '{{ graphql_engine_resource_limits_memory }}'
{% endif %}
{% endif %}
{% if k8s_distribution == 'k8s' %}
      securityContext:
        runAsUser: {{ graphql_engine_run_as_user }}
{% endif %}
{% if graphql_engine_volumes is defined and graphql_engine_volumes %}
      volumeMounts:
{%   for volume in graphql_engine_volumes %}
      - name: '{{ volume.name }}'
        mountPath: '{{ volume.mount_path }}'
{%     if volume.read_only is defined and volume.read_only %}
        readOnly: true
{%     endif %}
{%   endfor %}
{% endif %}
{% if graphql_engine_volumes is defined and graphql_engine_volumes %}
    volumes:
{%   for volume in graphql_engine_volumes %}
{%     if volume.source is defined and volume.source %}
    - name: '{{ volume.name }}'
      {{ volume.source | to_nice_yaml(indent=2) | indent(6) }}
{%     endif %}
{%   endfor %}
{% endif %}
{% if graphql_engine_tolerations %}
    tolerations:
    {{ graphql_engine_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if graphql_engine_image_pull_secret %}
    imagePullSecrets:
    - name: {{ graphql_engine_image_pull_secret }}
{% endif %}

```
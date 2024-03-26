



# moodle-spec.yaml.j2
  
---  
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
schedule: "{{ moodle_cronjob_schedule }}"
suspend: {{ true if cr_state == 'suspended' else moodle_cronjob_suspend }}
concurrencyPolicy: {{ moodle_cronjob_concurrency_policy }}
successfulJobsHistoryLimit: {{ moodle_cronjob_success_limit }}
startingDeadlineSeconds: {{ moodle_cronjob_starting_deadline_seconds }}
failedJobsHistoryLimit: {{ moodle_cronjob_failed_limit }}
jobTemplate:
  spec:
    completions: {{ moodle_cronjob_completions }}
    parallelism: {{ moodle_cronjob_parallelism }}
    backoffLimit: {{ moodle_cronjob_backoff_limit }}
    activeDeadlineSeconds: {{ moodle_cronjob_active_deadline_seconds }}
{% if moodle_cronjob_ttl_seconds_after_finished is defined and moodle_cronjob_ttl_seconds_after_finished %}
    ttlSecondsAfterFinished: {{ moodle_cronjob_ttl_seconds_after_finished }}
{% endif %}
    template:
      {{ metadata() | indent(width=6) }}
      spec:
        restartPolicy: Never
        automountServiceAccountToken: false
        containers:
        - name: 'moodle-cronjob'
          image: '{{ moodle_image }}'
          env:
          - {{ moodle_cronjob_php_fpm_database_check_socket | to_nice_yaml(indent=2) | indent(12) }}
          - name: PHP_FPM_LISTEN_ALLOWED_CLIENTS
            value: any
          - name: PHP_FPM_PROCESS_CONTROL_TIMEOUT
            value: '{{ moodle_cronjob_php_fpm_config_process_control_timeout }}'
{% if moodle_cronjob_envvars is defined and moodle_cronjob_envvars %}
{%   for moodle_cronjob_envvar in moodle_cronjob_envvars %}
          - name: {{ moodle_cronjob_envvar.name }}
{%     if moodle_cronjob_envvar.value is defined %}
            value: {{ moodle_cronjob_envvar.value }}
{%     endif %}
{%     if moodle_cronjob_envvar.source is defined %}
            valueFrom:
              {{ moodle_cronjob_envvar.source | indent(14) }}
{%     endif %}
{%   endfor %}
{% endif %}
{% if moodle_cronjob_command is defined and moodle_cronjob_command %}
{%   if moodle_cronjob_command is string %}
          command: {{ moodle_cronjob_command }}
{%   elif moodle_cronjob_command | type_debug == 'list' %}
          command:
          {{ moodle_cronjob_command | to_nice_yaml(indent=2) | indent(10) }}
{%   endif %}
{% endif %}
{% if moodle_cronjob_args is defined and moodle_cronjob_args %}
{%   if moodle_cronjob_args is string %}
          args: {{ moodle_cronjob_args }}
{%   elif moodle_cronjob_args | type_debug == 'list' %}
          args:
          {{ moodle_cronjob_args | to_nice_yaml(indent=2) | indent(10) }}
{%   endif %}
{% endif %}
          ports:
          - containerPort: 9000
          imagePullPolicy: IfNotPresent
{% if moodle_cronjob_resource_requests or moodle_cronjob_resource_limits %}
          resources:
{% if moodle_cronjob_resource_requests %}
            requests:
              cpu: '{{ moodle_cronjob_resource_requests_cpu }}'
              memory: '{{ moodle_cronjob_resource_requests_memory }}'
{% endif %}
{% if moodle_cronjob_resource_limits %}
            limits:
              cpu: '{{ moodle_cronjob_resource_limits_cpu }}'
              memory: '{{ moodle_cronjob_resource_limits_memory }}'
{% endif %}
{% endif %}
          volumeMounts:
          - mountPath: /etc/php.d/99-php-extra.ini
            name: php-fpm-extra-config
            subPath: php-extra.ini
          - mountPath: /etc/php-fpm.d/zz-php-fpm-extra.conf
            name: php-fpm-extra-config
            subPath: php-fpm-extra.conf
          - mountPath: '{{ moodle_volume_moodledata.mount_path }}'
            name: "{{ moodle_volume_moodledata.name }}"
{% if moodle_local_dir is defined and moodle_local_dir %}
          - mountPath: '{{ moodle_local_dir }}'
            name: localcache
{% endif %}
          - mountPath: '{{ moodle_app }}/config.php'
            name: config-php
            subPath: config.php
            readOnly: true
          - mountPath: {{ moodle_scripts_path }}
            name: scripts
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
        - name: "{{ moodle_volume_moodledata.name }}"
          {{ moodle_volume_moodledata.source | indent(10) }}
{% if moodle_local_dir is defined and moodle_local_dir %}
        - name: localcache
          emptyDir: {}
{% endif %}
        - name: config-php
          secret:
            secretName: '{{ moodle_secret_config }}'
            items:
            - key: config.php
              path: config.php
        - name: scripts
          configMap:
            name: '{{ moodle_cm_scripts }}'
            defaultMode: 0555
{% if moodle_cronjob_tolerations %}
        tolerations:
        {{ moodle_cronjob_tolerations | to_nice_yaml(indent=2) | indent(8) }}
{% endif %}
{% if moodle_image_pull_secret %}
        imagePullSecrets:
        - name: {{ moodle_image_pull_secret }}
{% endif %}
{% if moodle_cronjob_node_selector %}
        nodeSelector:
          {{ moodle_cronjob_node_selector | indent(10) }}
{% endif %}
{% if moodle_cronjob_affinity %}
        affinity:
          {{ moodle_cronjob_affinity | indent(10) }}
{% endif %}
  
```




# moodle-update-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
completions: 1
parallelism: 1
backoffLimit: 3
activeDeadlineSeconds: {{ moodle_update_job_active_deadline_seconds }}
{% if moodle_update_job_ttl_seconds_after_finished is defined and moodle_update_job_ttl_seconds_after_finished %}
ttlSecondsAfterFinished: {{ moodle_update_job_ttl_seconds_after_finished }}
{% endif %}
template:
  {{ metadata() | indent(width=2) }}
  spec:
    restartPolicy: Never
    automountServiceAccountToken: false
    containers:
    - name: 'moodle-update-job'
      image: '{{ moodle_image }}'
      env:
      - {{ moodle_update_job_php_fpm_database_check_socket | to_nice_yaml(indent=2) | indent(8) }}
      - name: PHP_FPM_LISTEN
        value: '127.0.0.1:9000'
      - name: PHP_FPM_LISTEN_ALLOWED_CLIENTS
        value: '127.0.0.1'
      - name: PHP_FPM_PROCESS_CONTROL_TIMEOUT
        value: '{{ moodle_update_job_php_fpm_config_process_control_timeout }}'
{% if moodle_update_job_command is defined and moodle_update_job_command %}
{%   if moodle_update_job_command is string %}
      command: {{ moodle_update_job_command }}
{%   elif moodle_update_job_command | type_debug == 'list' %}
      command:
      {{ moodle_update_job_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if moodle_update_job_args is defined and moodle_update_job_args %}
{%   if moodle_update_job_args is string %}
      args: {{ moodle_update_job_args }}
{%   elif moodle_update_job_args | type_debug == 'list' %}
      args:
      {{ moodle_update_job_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
      ports:
      - containerPort: 9000
      imagePullPolicy: {{ moodle_update_job_image_pull_policy | default('IfNotPresent') }}
{% if moodle_update_job_resource_requests or moodle_update_job_resource_limits %}
      resources:
{% if moodle_update_job_resource_requests %}
        requests:
          cpu: '{{ moodle_update_job_resource_requests_cpu }}'
          memory: '{{ moodle_update_job_resource_requests_memory }}'
{% endif %}
{% if moodle_update_job_resource_limits %}
        limits:
          cpu: '{{ moodle_update_job_resource_limits_cpu }}'
          memory: '{{ moodle_update_job_resource_limits_memory }}'
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
      - mountPath: "{{ moodle_muc_config_json_file }}"
        name: config-php
        subPath: "{{ moodle_muc_config_json_file | basename }}"
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
      {{ moodle_volume_moodledata.source | indent(6) }}
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
        - key: "{{ moodle_muc_config_json_file | basename }}"
          path: "{{ moodle_muc_config_json_file | basename }}"
    - name: scripts
      configMap:
        name: '{{ moodle_cm_scripts }}'
        defaultMode: 0555
{% if moodle_update_job_tolerations %}
    tolerations:
    {{ moodle_update_job_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if moodle_image_pull_secret %}
    imagePullSecrets:
    - name: {{ moodle_image_pull_secret }}
{% endif %}
{% if moodle_update_job_node_selector %}
    nodeSelector:
      {{ moodle_update_job_node_selector | indent(6) }}
{% endif %}
{% if moodle_update_job_affinity %}
    affinity:
      {{ moodle_update_job_affinity | indent(6) }}
{% endif %}

```
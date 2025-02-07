



# moodle-new-instance-spec.yaml.j2
  
---  
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
completions: 1
parallelism: 1
backoffLimit: 3
activeDeadlineSeconds: {{ moodle_new_instance_job_active_deadline_seconds }}
{% if moodle_new_instance_job_ttl_seconds_after_finished is defined and moodle_new_instance_job_ttl_seconds_after_finished %}
ttlSecondsAfterFinished: {{ moodle_new_instance_job_ttl_seconds_after_finished }}
{% endif %}
template:
  {{ metadata() | indent(width=2) }}
  spec:
    restartPolicy: Never
    automountServiceAccountToken: false
{% if k8s_distribution == 'k8s' %}
    initContainers:
    - name: 'data-dir-permissions'
      image: '{{ moodle_image }}'
      securityContext:
        runAsUser: 0
      command:
        - '/bin/bash'
        - '-c'
        - |
          chown ${CTR_USER_ID}:48 '{{ moodle_volume_moodledata.mount_path }}'
          chmod 0740 {{ moodle_volume_moodledata.mount_path }}
      volumeMounts:
      - mountPath: '{{ moodle_volume_moodledata.mount_path }}'
        name: "{{ moodle_volume_moodledata.name }}"
{% endif %}
    containers:
    - name: 'moodle-new-instance-job'
      image: '{{ moodle_image }}'
      env:
      - {{ moodle_new_instance_job_php_fpm_database_check_socket | to_nice_yaml(indent=2) | indent(8) }}
      - name: PHP_FPM_LISTEN
        value: '127.0.0.1:9000'
      - name: PHP_FPM_LISTEN_ALLOWED_CLIENTS
        value: '127.0.0.1'
      - name: PHP_FPM_PROCESS_CONTROL_TIMEOUT
        value: '{{ moodle_new_instance_job_php_fpm_config_process_control_timeout }}'
{% if moodle_redis_secret | default(false, true) %}
      - name: REDIS_PASSWORD
        valueFrom:
          secretKeyRef:
            name: "{{ moodle_redis_secret }}"
            key: "{{ moodle_redis_secret_auth_key }}"
{% endif %}
{% if moodle_new_instance_job_command is defined and moodle_new_instance_job_command %}
{%   if moodle_new_instance_job_command is string %}
      command: {{ moodle_new_instance_job_command }}
{%   elif moodle_new_instance_job_command | type_debug == 'list' %}
      command:
      {{ moodle_new_instance_job_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if moodle_new_instance_job_args is defined and moodle_new_instance_job_args %}
{%   if moodle_new_instance_job_args is string %}
      args: {{ moodle_new_instance_job_args }}
{%   elif moodle_new_instance_job_args | type_debug == 'list' %}
      args:
      {{ moodle_new_instance_job_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if moodle_new_instance_job_startup_probe | bool %}
      startupProbe:
        exec:
{%   if moodle_new_instance_job_startup_command is string %}
          command: {{ moodle_new_instance_job_startup_command }}
{%   elif moodle_new_instance_job_startup_command | type_debug == 'list' %}
          command:
          {{ moodle_new_instance_job_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%   endif %}
        initialDelaySeconds: {{ moodle_new_instance_job_startup_initial }}
        periodSeconds: {{ moodle_new_instance_job_startup_period }}
        timeoutSeconds: {{ moodle_new_instance_job_startup_timeout }}
        successThreshold: {{ moodle_new_instance_job_startup_success }}
        failureThreshold: {{ moodle_new_instance_job_startup_failure }}
{% endif %}
      ports:
      - containerPort: 9000
      imagePullPolicy: {{ moodle_new_instance_job_image_pull_policy | default('IfNotPresent') }}
{% if moodle_new_instance_job_resource_requests or moodle_new_instance_job_resource_limits %}
      resources:
{% if moodle_new_instance_job_resource_requests %}
        requests:
          cpu: '{{ moodle_new_instance_job_resource_requests_cpu }}'
          memory: '{{ moodle_new_instance_job_resource_requests_memory }}'
{% endif %}
{% if moodle_new_instance_job_resource_limits %}
        limits:
          cpu: '{{ moodle_new_instance_job_resource_limits_cpu }}'
          memory: '{{ moodle_new_instance_job_resource_limits_memory }}'
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
{% if moodle_new_instance_job_tolerations %}
    tolerations:
    {{ moodle_new_instance_job_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if moodle_image_pull_secret %}
    imagePullSecrets:
    - name: {{ moodle_image_pull_secret }}
{% endif %}
{% if moodle_new_instance_job_node_selector %}
    nodeSelector:
      {{ moodle_new_instance_job_node_selector | indent(6) }}
{% endif %}
{% if moodle_new_instance_job_affinity %}
    affinity:
      {{ moodle_new_instance_job_affinity | indent(6) }}
{% endif %}
  
```
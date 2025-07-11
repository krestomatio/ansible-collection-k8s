



# ganesha-spec.yaml.j2

---
```

{% macro metadata() %}{% include common_path + '/metadata.j2' ignore missing %}{% endmacro %}
replicas: {{ 0 if cr_state == 'suspended' else 1 }}
serviceName: '{{ ganesha_service }}'
selector:
  matchLabels:
    app: '{{ ganesha_appname }}'
template:
  {{ metadata() | indent(width=2) }}
  spec:
    terminationGracePeriodSeconds: {{ ganesha_term_grace_period }}
    automountServiceAccountToken: false
{% if (ganesha_init_containers is defined and ganesha_init_containers) or k8s_distribution == 'k8s' %}
    initContainers:
{%   if ganesha_init_containers is defined and ganesha_init_containers %}
    {{ ganesha_init_containers | indent(4) }}
{%   endif %}
{%   if k8s_distribution == 'k8s' and ganesha_export_owner_mode_set %}
    - name: 'data-dir-permissions'
      image: '{{ ganesha_image }}'
      securityContext:
        runAsUser: 0
      command:
        - '/bin/bash'
        - '-c'
        - |
          chown {{ ganesha_pvc_data_userid }}:{{ ganesha_pvc_data_groupid }} '{{ ganesha_pvc_data_mount_path }}'
          chmod {{ ganesha_export_mode }} '{{ ganesha_pvc_data_mount_path }}'
      volumeMounts:
      - mountPath: '{{ ganesha_pvc_data_mount_path }}'
        name: {{ ganesha_pvc_data }}
{%   endif %}
{% endif %}
    containers:
    - name: '{{ ganesha_container }}'
      image: '{{ ganesha_image }}'
      imagePullPolicy: '{{ ganesha_image_pull_policy | default('IfNotPresent') }}'
      env:
      - name: NFS_GANESHA_CONF_DIR
        value: "{{ ganesha_conf_dir }}"
      - name: NFS_GANESHA_CONF_FILE
        value: "{{ ganesha_conf_file }}"
      - name: NFS_GANESHA_CONF_EXTRA_FILE
        value: "{{ ganesha_conf_extra_file }}"
      - name: NFS_GANESHA_CONF_NO_OVERWRITE
        value: "true"
      - name: NFS_GANESHA_GRACE_PERIOD
        value: "'{{ ganesha_conf_grace_period }}'"
      - name: NFS_GANESHA_EXPORT_DIR
        value: "{{ ganesha_pvc_data_mount_path }}"
      - name: NFS_GANESHA_EXPORT_ID
        value: "'{{ ganesha_conf_export_id }}'"
      - name: NFS_GANESHA_EXPORT_SQUASH
        value: "{{ ganesha_conf_export_squash }}"
      - name: NFS_GANESHA_EXPORT_HWMARK
        value: "{{ ganesha_conf_export_hwmark }}"
      - name: NFS_GANESHA_LOG_LEVEL
        value: "{{ ganesha_conf_log_level }}"
      - name: NFS_GANESHA_PORT
        value: "{{ ganesha_port }}"
      - name: NFS_GANESHA_RQUOTA_PORT
        value: "{{ ganesha_rquota_port }}"
      - name: NFS_GANESHA_RUN_DIR
        value: "{{ ganesha_run_dir }}"
      - name: DBUS_RUN_WAIT
        value: "{{ ganesha_dbus_separete_container }}"
{% if ganesha_envvars is defined and ganesha_envvars %}
{%   for ganesha_envvar in ganesha_envvars %}
      - name: {{ ganesha_envvar.name }}
{%     if ganesha_envvar.value is defined %}
        value: {{ ganesha_envvar.value }}
{%     endif %}
{%     if ganesha_envvar.source is defined %}
        valueFrom:
          {{ ganesha_envvar.source | indent(10) }}
{%     endif %}
{%   endfor %}
{% endif %}
      ports:
      - name: nfs-tcp
        containerPort: {{ ganesha_port }}
        protocol: TCP
      # Issue: https://github.com/kubernetes/kubernetes/issues/39188
      # - name: nfs-udp
      #   containerPort: {{ ganesha_port }}
      #   protocol: UDP
{% if ganesha_rquota %}
      - name: rquota-tcp
        containerPort: {{ ganesha_rquota_port }}
        protocol: TCP
      # Issue: https://github.com/kubernetes/kubernetes/issues/39188
      # - name: rquota-udp
      #   containerPort: {{ ganesha_rquota_port }}
      #   protocol: UDP
{% endif %}
{% if ganesha_command is defined and ganesha_command %}
{%   if ganesha_command is string %}
      command: {{ ganesha_command }}
{%   elif ganesha_command | type_debug == 'list' %}
      command:
      {{ ganesha_command | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if ganesha_args is defined and ganesha_args %}
{%   if ganesha_args is string %}
      args: {{ ganesha_args }}
{%   elif ganesha_args | type_debug == 'list' %}
      args:
      {{ ganesha_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
{% if ganesha_startup_probe %}
      startupProbe:
{%   if ganesha_startup_command is defined and ganesha_startup_command %}
        exec:
{%     if ganesha_startup_command is string %}
          command: {{ ganesha_startup_command }}
{%     elif ganesha_startup_command | type_debug == 'list' %}
          command:
          {{ ganesha_startup_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif ganesha_startup_path is defined and ganesha_startup_path %}
        httpGet:
          path: '{{ ganesha_startup_path }}'
          port: {{ ganesha_startup_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ ganesha_startup_host }}'
{%   elif ganesha_startup_tcp_socket is defined and ganesha_startup_tcp_socket %}
        tcpSocket:
          port: {{ ganesha_startup_tcp_socket }}
{%   endif %}
        initialDelaySeconds: {{ ganesha_startup_initial }}
        periodSeconds: {{ ganesha_startup_period }}
        timeoutSeconds: {{ ganesha_startup_timeout }}
        successThreshold: {{ ganesha_startup_success }}
        failureThreshold: {{ ganesha_startup_failure }}
{% endif %}
{% if ganesha_readiness_probe %}
      readinessProbe:
{%   if ganesha_readiness_command is defined and ganesha_readiness_command %}
        exec:
{%     if ganesha_readiness_command is string %}
          command: {{ ganesha_readiness_command }}
{%     elif ganesha_readiness_command | type_debug == 'list' %}
          command:
          {{ ganesha_readiness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif ganesha_readiness_path is defined and ganesha_readiness_path %}
        httpGet:
          path: '{{ ganesha_readiness_path }}'
          port: {{ ganesha_readiness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ ganesha_readiness_host }}'
{%   elif ganesha_readiness_tcp_socket is defined and ganesha_readiness_tcp_socket %}
        tcpSocket:
          port: {{ ganesha_readiness_tcp_socket }}
{%   endif %}
        initialDelaySeconds: {{ ganesha_readiness_initial }}
        periodSeconds: {{ ganesha_readiness_period }}
        timeoutSeconds: {{ ganesha_readiness_timeout }}
        successThreshold: {{ ganesha_readiness_success }}
        failureThreshold: {{ ganesha_readiness_failure }}
{% endif %}
{% if ganesha_liveness_probe %}
      livenessProbe:
{%   if ganesha_liveness_command is defined and ganesha_liveness_command %}
        exec:
{%     if ganesha_liveness_command is string %}
          command: {{ ganesha_liveness_command }}
{%     elif ganesha_liveness_command | type_debug == 'list' %}
          command:
          {{ ganesha_liveness_command | to_nice_yaml(indent=2) | indent(10) }}
{%     endif %}
{%   elif ganesha_liveness_path is defined and ganesha_liveness_path %}
        httpGet:
          path: '{{ ganesha_liveness_path }}'
          port: {{ ganesha_liveness_port }}
          httpHeaders:
          - name: 'Host'
            value: '{{ ganesha_liveness_host }}'
{%   elif ganesha_liveness_tcp_socket is defined and ganesha_liveness_tcp_socket %}
        tcpSocket:
          port: {{ ganesha_liveness_tcp_socket }}
{%   endif %}
        initialDelaySeconds: {{ ganesha_liveness_initial }}
        periodSeconds: {{ ganesha_liveness_period }}
        timeoutSeconds: {{ ganesha_liveness_timeout }}
        successThreshold: {{ ganesha_liveness_success }}
        failureThreshold: {{ ganesha_liveness_failure }}
{% endif %}
{% if ganesha_resource_requests | bool or ganesha_resource_limits | bool %}
      resources:
{%   if ganesha_resource_requests | bool %}
        requests:
          cpu: '{{ ganesha_resource_requests_cpu }}'
          memory: '{{ ganesha_resource_requests_memory }}'
{%   endif %}
{%   if ganesha_resource_limits | bool %}
        limits:
          cpu: '{{ ganesha_resource_limits_cpu }}'
          memory: '{{ ganesha_resource_limits_memory }}'
{%   endif %}
{% endif %}
      securityContext:
        allowPrivilegeEscalation: {{ ganesha_allow_privilege_escalation | default('false') }}
        readOnlyRootFilesystem: {{ ganesha_read_only_root_filesystem | default('true') }}
{% if ganesha_capabilities is defined and ganesha_capabilities %}
        capabilities:
          {{ ganesha_capabilities | indent(10) }}
{% endif %}
{% if ganesha_run_as_user is defined and ganesha_run_as_user %}
        runAsUser: {{ ganesha_run_as_user }}
{% endif %}
{% if ganesha_security_context is defined and ganesha_security_context %}
        {{ ganesha_security_context | indent(8) }}
{% endif %}
      terminationMessagePolicy: "{{ ganesha_termination_message_policy | default('FallbackToLogsOnError') }}"
      volumeMounts:
      - name: nfs-ganesha-run
        mountPath: '{{ ganesha_run_dir }}'
      - name: dbus-run
        mountPath: /var/run/dbus
        readOnly: true
      - name: nfs-ganesha-lib
        mountPath: '{{ ganesha_lib_dir }}'
      - name: nfs-ganesha-tmp
        mountPath: '{{ ganesha_tmp_dir }}'
      - name: ganesha-config
        mountPath: '{{ ganesha_conf_file }}'
        subPath: ganesha.conf
      - name: ganesha-config
        mountPath: '{{ ganesha_conf_extra_file }}'
        subPath: ganesha-extra.conf
      - name: {{ ganesha_pvc_data }}
        mountPath: '{{ ganesha_pvc_data_mount_path }}'
{% if ganesha_dbus_separete_container is defined and ganesha_dbus_separete_container %}
    - name: '{{ dbus_container }}'
      image: '{{ dbus_image }}'
      imagePullPolicy: '{{ dbus_image_pull_policy | default('IfNotPresent') }}'
{%   if dbus_command is defined and dbus_command %}
{%     if dbus_command is string %}
      command: {{ dbus_command }}
{%     elif dbus_command | type_debug == 'list' %}
      command:
      {{ dbus_command | to_nice_yaml(indent=2) | indent(6) }}
{%     endif %}
{%   endif %}
{% if dbus_args is defined and dbus_args %}
{%   if dbus_args is string %}
      args: {{ dbus_args }}
{%   elif dbus_args | type_debug == 'list' %}
      args:
      {{ dbus_args | to_nice_yaml(indent=2) | indent(6) }}
{%   endif %}
{% endif %}
      securityContext:
        allowPrivilegeEscalation: {{ dbus_allow_privilege_escalation | default('false') }}
        readOnlyRootFilesystem: {{ dbus_read_only_root_filesystem | default('true') }}
{%   if dbus_capabilities is defined and dbus_capabilities %}
        capabilities:
          {{ dbus_capabilities | indent(10) }}
{%   endif %}
{%   if dbus_run_as_user is defined and dbus_run_as_user %}
        runAsUser: {{ dbus_run_as_user }}
{%   endif %}
{%   if dbus_security_context is defined and dbus_security_context %}
        {{ dbus_security_context | indent(8) }}
{%   endif %}
      terminationMessagePolicy: "{{ dbus_termination_message_policy | default('FallbackToLogsOnError') }}"
      volumeMounts:
      - name: dbus-run
        mountPath: /var/run/dbus
      - name: dbus-lib
        mountPath: /var/lib/dbus
{% endif %}
    volumes:
    - name: nfs-ganesha-lib
      emptyDir: {}
    - name: nfs-ganesha-tmp
      emptyDir:
        medium: Memory
    - name: nfs-ganesha-run
      emptyDir:
        medium: Memory
    - name: dbus-run
      emptyDir:
        medium: Memory
    - name: dbus-lib
      emptyDir: {}
    - name: ganesha-config
      configMap:
        name: '{{ ganesha_cm }}'
        defaultMode: 0664
        items:
        - key: ganesha.conf
          path: ganesha.conf
        - key: ganesha-extra.conf
          path: ganesha-extra.conf
{% if ganesha_tolerations is defined and ganesha_tolerations %}
    tolerations:
    {{ ganesha_tolerations | to_nice_yaml(indent=2) | indent(4) }}
{% endif %}
{% if ganesha_image_pull_secret is defined and ganesha_image_pull_secret %}
    imagePullSecrets:
    - name: {{ ganesha_image_pull_secret }}
{% endif %}
{% if ganesha_node_selector %}
    nodeSelector:
      {{ ganesha_node_selector | indent(6) }}
{% endif %}
{% if ganesha_affinity %}
    affinity:
      {{ ganesha_affinity | indent(6) }}
{% endif %}
volumeClaimTemplates:
  {{ ganesha_volume_claim_template | to_nice_yaml(indent=2) | indent(2) }}

```
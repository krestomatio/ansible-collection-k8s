



# ganesha.yml
  
---
## ganesha_state
  
```

'{{ state }}'
  
```
## ganesha_appname
  
```

'{{ meta_name }}-nfs'
  
```
## ganesha_image
  
```

quay.io/krestomatio/nfs-ganesha:5.5.3@sha256:a01796c7cf5aee7dca613e6fa90cd784d63a188000066848fb29b8167057ee8f
...
  
```
## ganesha_image_pull_secret
  
```

'{{ image_pull_secret }}'
  
```
## ganesha_sts
  
```

'{{ ganesha_appname }}-sts'
  
```
## ganesha_container
  
```

nfs-ganesha
...
  
```
## ganesha_container_group
  
```

'{{ ganesha_container.replace(''-'', ''_'') }}'
  
```
## ganesha_args
  
```

false
...
  
```
## ganesha_startup_probe
  
```

true
...
  
```
## ganesha_startup_tcp_socket
  
```

'{{ ganesha_port }}'
  
```
## ganesha_startup_initial
  
```

2
...
  
```
## ganesha_startup_period
  
```

5
...
  
```
## ganesha_startup_timeout
  
```

1
...
  
```
## ganesha_startup_success
  
```

1
...
  
```
## ganesha_startup_failure
  
```

3
...
  
```
## ganesha_readiness_probe
  
```

true
...
  
```
## ganesha_readiness_tcp_socket
  
```

'{{ ganesha_port }}'
  
```
## ganesha_readiness_initial
  
```

2
...
  
```
## ganesha_readiness_period
  
```

5
...
  
```
## ganesha_readiness_timeout
  
```

1
...
  
```
## ganesha_readiness_success
  
```

1
...
  
```
## ganesha_readiness_failure
  
```

3
...
  
```
## ganesha_liveness_probe
  
```

true
...
  
```
## ganesha_liveness_tcp_socket
  
```

'{{ ganesha_port }}'
  
```
## ganesha_liveness_initial
  
```

5
...
  
```
## ganesha_liveness_period
  
```

10
...
  
```
## ganesha_liveness_timeout
  
```

10
...
  
```
## ganesha_liveness_success
  
```

1
...
  
```
## ganesha_liveness_failure
  
```

3
...
  
```
## ganesha_resource_requests
  
```

true
...
  
```
## ganesha_resource_requests_cpu
  
```

25m
...
  
```
## ganesha_resource_requests_memory
  
```

64Mi
...
  
```
## ganesha_resource_limits
  
```

false
...
  
```
## ganesha_resource_limits_cpu
  
```

1
...
  
```
## ganesha_resource_limits_memory
  
```

1Gi
...
  
```
## ganesha_term_grace_period
  
```

30
...
  
```
## ganesha_tolerations
  
```

false
...
  
```
## ganesha_node_selector
  
```

false
...
  
```
## ganesha_affinity
  
```

false
...
  
```
## ganesha_port
  
```

2049
...
  
```
## ganesha_run_as_user
  
```

0
...
  
```
## ganesha_capabilities
  
```

"drop:\n  - ALL\nadd:\n  - CHOWN\n  - DAC_OVERRIDE\n  - DAC_READ_SEARCH\n  - FOWNER\n\
  \  - FSETID\n  - KILL\n  - SETGID\n  - SETUID\n  - SETPCAP\n  - NET_BIND_SERVICE\n\
  \  - NET_RAW\n  - SYS_CHROOT\n  - MKNOD\n  - AUDIT_WRITE\n"
  
```
## dbus_container
  
```

dbus
...
  
```
## dbus_image
  
```

'{{ ganesha_image }}'
  
```
## dbus_command
  
```

- /usr/bin/dbus-daemon
- --nofork
- --nopidfile
- --nosyslog
- --system
  
```
## dbus_capabilities
  
```

"drop:\n  - ALL\nadd:\n  - SETGID\n  - SETPCAP\n  - SETUID\n"
  
```
## dbus_run_as_user
  
```

'{{ ganesha_run_as_user }}'
  
```
## ganesha_service
  
```

'{{ ganesha_appname }}-service'
  
```
## ganesha_service_spec
  
```

"{% if ganesha_service_type is defined %}\ntype: {{ ganesha_service_type }}\n{% endif\
  \ %}\n{% if ganesha_service_cluster_ip is defined %}\nclusterIP: {{ ganesha_service_cluster_ip\
  \ }}\n{% endif %}\n{% if ganesha_service_session_affinity is defined %}\nsessionAffinity:\
  \ {{ ganesha_service_session_affinity }}\n{% endif %}\n{% if ganesha_service_session_affinity_timeout\
  \ is defined %}\nsessionAffinityConfig:\n  clientIP:\n    timeoutSeconds: {{ ganesha_service_session_affinity_timeout\
  \ }}\n{% endif %}\nselector:\n  app: '{{ ganesha_appname }}'\nports:\n- name: nfs-tcp\n\
  \  port: {{ ganesha_port }}\n  protocol: TCP\n  targetPort: {{ ganesha_port }}\n\
  # Issue: https://github.com/kubernetes/kubernetes/issues/39188\n# - name: nfs-udp\n\
  #   port: {{ ganesha_port }}\n#   protocol: UDP\n#   targetPort: {{ ganesha_port\
  \ }}\n{% if ganesha_rquota %}\n- name: rquota-tcp\n  port: {{ ganesha_rquota_port\
  \ }}\n  protocol: TCP\n  targetPort: {{ ganesha_rquota_port }}\n# Issue: https://github.com/kubernetes/kubernetes/issues/39188\n\
  # - name: rquota-udp\n#   port: {{ ganesha_rquota_port }}\n#   protocol: UDP\n#\
  \   targetPort: {{ ganesha_rquota_port }}\n{% endif %}\n"
  
```
## ganesha_generated_nfs_sc
  
```

'{{ (ganesha_appname | truncate(41,true,'''')) + ''-'' + (cr_uid | truncate(18,true,''''))
  }}-sc'
  
```
## ganesha_generated_nfs_sc_needed
  
```

false
...
  
```
## ganesha_generated_nfs_sc_parameters
  
```

'server: "{{ ganesha_service + ''.'' + meta_namespace }}"

  share: "{{ ganesha_generated_nfs_sc_share | default(''/'') }}"

  {% if ganesha_generated_nfs_sc_mount_permissions is defined and ganesha_generated_nfs_sc_mount_permissions
  %}

  mountPermissions: "{{ ganesha_generated_nfs_sc_mount_permissions }}"

  {% endif %}

  {% if ganesha_generated_nfs_sc_extra_parameters is defined and ganesha_generated_nfs_sc_extra_parameters
  %}

  {{ ganesha_generated_nfs_sc_extra_parameters }}

  {% endif %}'
  
```
## ganesha_generated_nfs_sc_mount_options
  
```

false
...
  
```
## ganesha_generated_nfs_sc_provisioner
  
```

nfs.csi.k8s.io
...
  
```
## ganesha_generated_nfs_sc_allow_volume_expansion
  
```

'{{ ganesha_pvc_data_autoexpansion }}'
  
```
## ganesha_generated_nfs_sc_reclaim_policy
  
```

Delete
...
  
```
## ganesha_generated_nfs_sc_volume_binding_mode
  
```

Immediate
...
  
```
## ganesha_pvc_data
  
```

'{{ ganesha_appname }}-data-pvc'
  
```
## ganesha_pvc_data_storage_access_mode
  
```

ReadWriteOnce
...
  
```
## ganesha_pvc_data_storage_class_name
  
```

false
...
  
```
## ganesha_pvc_data_mode
  
```

'{{ ganesha_export_mode }}'
  
```
## ganesha_pvc_data_mount_path
  
```

'{{ ganesha_export_dir }}'
  
```
## ganesha_pvc_data_userid
  
```

'{{ ganesha_export_userid }}'
  
```
## ganesha_pvc_data_groupid
  
```

'{{ ganesha_export_groupid }}'
  
```
## ganesha_pvc_data_spec
  
```

"{% if ganesha_pvc_data_storage_class_name is defined and ganesha_pvc_data_storage_class_name\
  \ %}\nstorageClassName: {{ ganesha_pvc_data_storage_class_name }}\n{% endif %}\n\
  accessModes:\n  - '{{ ganesha_pvc_data_storage_access_mode }}'\nresources:\n  requests:\n\
  \    storage: '{{ ganesha_pvc_data_size }}'\n"
  
```
## ganesha_pvc_data_current_size
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=ganesha_sts).spec.volumeClaimTemplates[0].spec.resources.requests.storage
  | default('''') }}'
  
```
## ganesha_pvc_data_size
  
```

'{{ ganesha_pvc_data_size_gib | string + ''Gi'' if ganesha_pvc_data_autoexpansion
  else ganesha_pvc_data_current_size | default(''1Gi'', true) }}'
  
```
## ganesha_pvc_data_size_gib
  
```

'{{ cr_status_properties[routine_pvc_autoexpand_info_keyname].autoexpandSizeGib |
  default(ganesha_pvc_data_autoexpansion_increment_gib) }}'
  
```
## ganesha_pvc_data_autoexpansion
  
```

false
...
  
```
## ganesha_pvc_data_autoexpansion_increment_gib
  
```

1
...
  
```
## ganesha_pvc_data_autoexpansion_cap_gib
  
```

5
...
  
```
## ganesha_pvc_data_current_labels
  
```

'{{ lookup(''k8s'', api_version=''v1'', kind=''StatefulSet'', namespace=meta_namespace,
  resource_name=ganesha_sts).spec.volumeClaimTemplates[0].metadata.labels | default('''')
  }}'
  
```
## ganesha_cm
  
```

'{{ ganesha_appname }}-cm'
  
```
## ganesha_cm_data
  
```

"ganesha.conf: |\n  {{ ganesha_config | indent(2) }}\nganesha-extra.conf: |\n  {{\
  \ ganesha_extra_config | indent(2) }}\n"
  
```
## ganesha_config
  
```

"NFS_CORE_PARAM {\n    Protocols = 4;\n    NFS_Port = {{ ganesha_port }};\n    Rquota_Port\
  \ = {{ ganesha_rquota_port }};\n    fsid_device = true;\n}\nNFS_KRB5 {\n    Active_krb5\
  \ = false;\n}\nEXPORT_DEFAULTS {\n    SecType = sys;\n}\n%include \"{{ ganesha_conf_extra_file\
  \ }}\"\n"
  
```
## ganesha_extra_config
  
```

"NFSv4 {\n    Grace_Period = {{ ganesha_conf_grace_period }};\n}\nMDCACHE {\n    Entries_HWMark\
  \ = {{ ganesha_conf_export_hwmark }};\n}\nEXPORT {\n    Export_Id = {{ ganesha_conf_export_id\
  \ }};\n    Path = \"{{ ganesha_conf_export_path }}\";\n    Pseudo = {{ ganesha_conf_export_pseudo\
  \ }};\n    Access_Type = {{ ganesha_conf_export_access_type }};\n    Squash = {{\
  \ ganesha_conf_export_squash }};\n    FSAL {\n        Name = {{ ganesha_conf_fsal\
  \ }};\n    }\n}\nLOG {\n    COMPONENTS {\n        ALL = {{ ganesha_conf_log_level\
  \ }};\n    }\n}\n{% if ganesha_extra_block_config is defined and ganesha_extra_block_config\
  \ %}\n{{ ganesha_extra_block_config }}\n{% endif %}\n"
  
```
## ganesha_extra_block_config
  
```

''
  
```
## ganesha_dbus_separete_container
  
```

true
...
  
```
## ganesha_lib_dir
  
```

/usr/local/var/lib/nfs/ganesha
...
  
```
## ganesha_conf_dir
  
```

/usr/local/etc/ganesha
...
  
```
## ganesha_run_dir
  
```

/usr/local/var/run/ganesha
...
  
```
## ganesha_tmp_dir
  
```

/tmp
...
  
```
## ganesha_rquota
  
```

true
...
  
```
## ganesha_rquota_port
  
```

875
...
  
```
## ganesha_conf_file
  
```

'{{ ganesha_conf_dir }}/ganesha.conf'
  
```
## ganesha_conf_extra_file
  
```

'{{ ganesha_conf_dir }}/ganesha-extra.conf'
  
```
## ganesha_conf_grace_period
  
```

90
...
  
```
## ganesha_conf_export_path
  
```

'{{ ganesha_export_dir }}'
  
```
## ganesha_conf_export_pseudo
  
```

/
...
  
```
## ganesha_conf_export_id
  
```

1
...
  
```
## ganesha_conf_export_access_type
  
```

RW
...
  
```
## ganesha_conf_export_squash
  
```

no_root_squash
...
  
```
## ganesha_conf_export_hwmark
  
```

100000
...
  
```
## ganesha_conf_fsal
  
```

VFS
...
  
```
## ganesha_conf_log_level
  
```

EVENT
...
  
```
## ganesha_export_owner_mode_set
  
```

true
...
  
```
## ganesha_export_dir
  
```

/export
...
  
```
## ganesha_export_userid
  
```

0
...
  
```
## ganesha_export_groupid
  
```

0
...
  
```
## ganesha_export_mode
  
```

'0700'
  
```
## ganesha_vpa
  
```

'{{ ganesha_appname }}-vpa'
  
```
## ganesha_vpa_spec
  
```

false
...
  
```
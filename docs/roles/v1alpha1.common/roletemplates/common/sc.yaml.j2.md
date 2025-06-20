



# sc.yaml.j2

---
```

# {{ name }} storage class
---
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
{% include common_path + '/metadata.j2' ignore missing %}
{% if sc_parameters is defined and sc_parameters %}
parameters:
  {{ sc_parameters | indent(2) }}
{% endif %}
{% if sc_mount_options is defined and sc_mount_options %}
mountOptions:
  {{ sc_mount_options | to_nice_yaml(indent=2) | indent(2) }}
{% endif %}
{% if sc_provisioner is defined and sc_provisioner %}
provisioner: '{{ sc_provisioner }}'
{% endif %}
{% if sc_allow_volume_expansion is defined and sc_allow_volume_expansion %}
allowVolumeExpansion: {{ sc_allow_volume_expansion }}
{% endif %}
{% if sc_reclaim_policy is defined and sc_reclaim_policy %}
reclaimPolicy: {{ sc_reclaim_policy  }}
{% endif %}
{% if sc_volume_binding_mode is defined and sc_volume_binding_mode %}
volumeBindingMode: {{ sc_volume_binding_mode }}
{% endif %}

```
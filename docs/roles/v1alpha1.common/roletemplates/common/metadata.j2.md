



# metadata.j2
  
---  
```

{% set default_name = meta_name + '-' + name %}
metadata:
  name: '{{ metadata_name | default(default_name) }}'
{% if namespaced | default(true) %}
  namespace: '{{ metadata_namespace | default(meta_namespace) }}'
{% endif %}
  labels:
    app: '{{ metadata_app | default(metadata_name) | default(default_name) }}'
    app.kubernetes.io/name: '{{ metadata_app | default(metadata_name) | default(default_name) }}'
    app.kubernetes.io/instance: '{{ meta_name }}'
    app.kubernetes.io/managed-by: ansible
{% if meta_app_part_of | default(false) != false %}
    app.kubernetes.io/part-of: "{{ meta_app_part_of }}"
{% endif %}
{% if meta_app_created_by | default(false) != false %}
    app.kubernetes.io/created_by: {{ meta_app_created_by }}
{% endif %}
{% if inventory_uuid | default(false) != false and inventory_include %}
    {{ cr_group }}/inventory: '{{ inventory_uuid }}'
{% endif %}
{% if cr_uid | default(false,true) != false %}
    {{ cr_group }}/cr_uid: '{{ cr_uid }}'
{% endif %}
{% if component | default(false) != false %}
    app.kubernetes.io/component: '{{ component }}'
{% endif %}
{% if runtime | default(false) != false %}
    app.openshift.io/runtime: '{{ runtime }}'
{% endif %}
{% if cr_version | default(false) != false %}
    app.kubernetes.io/version: '{{ cr_version }}'
{% endif %}
{% if common_labels | default(false) != false %}
    {{ common_labels | indent(width=4) }}
{% endif %}
{% if extra_labels | default(false) != false %}
    {{ extra_labels | indent(width=4) }}
{% endif %}
{% if (annotations | default(false) != false) or (connects_to | default(false) != false) or (inventory_annotation_hostvars | default(false) != false and inventory_include)%}
  annotations:
{% if connects_to | default(false) != false %}
    app.openshift.io/connects-to: '{{ connects_to }}'
{% endif %}
{% if inventory_annotation_hostvars | default(false) != false and inventory_include %}
    {{ cr_group }}/inventory-hostvars: '{{ inventory_annotation_hostvars | to_json | indent( width=4) }}'
{% endif %}
{% if annotation_version_hash | default(false) != false %}
    {{ cr_group }}/version-hash: '{{ annotation_version_hash }}'
{% endif %}
{% if annotations | default(false) != false %}
    {{ annotations | indent( width=4) }}
{% endif %}
{% endif %}
  
```
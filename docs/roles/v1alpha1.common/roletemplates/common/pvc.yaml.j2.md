



# pvc.yaml.j2

---
```

# {{ name }} persistent volume claim
---
kind: PersistentVolumeClaim
apiVersion: v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if pvc_spec != false %}
spec:
  {{ pvc_spec | indent(width=2) }}
{% endif %}

```




# pv.yaml.j2

---
```

# {{ name }} persistent volume
---
kind: PersistentVolume
apiVersion: v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if pv_spec != false %}
spec:
  {{ pv_spec | indent(width=2) }}
{% endif %}

```
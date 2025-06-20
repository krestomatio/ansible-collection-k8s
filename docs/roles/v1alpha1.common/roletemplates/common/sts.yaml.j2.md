



# sts.yaml.j2

---
```

# {{ name }} statefulset
---
kind: StatefulSet
apiVersion: apps/v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if sts_spec != false %}
spec:
  {{ sts_spec | indent(width=2) }}
{% endif %}

```
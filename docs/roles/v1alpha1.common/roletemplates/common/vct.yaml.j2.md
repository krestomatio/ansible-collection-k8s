



# vct.yaml.j2

---
```

# volumeClaimTemplate
{% include common_path + '/metadata.j2' ignore missing %}
{% if pvc_spec != false %}
spec:
  {{ pvc_spec | indent(width=2) }}
{% endif %}

```
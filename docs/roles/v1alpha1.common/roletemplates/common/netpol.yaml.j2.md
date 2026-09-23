



# netpol.yaml.j2

---
```

# {{ name }} network policy
---
kind: NetworkPolicy
apiVersion: v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if netpol_spec != false %}
spec:
  {{ netpol_spec | indent(width=2) }}
{% endif %}

```
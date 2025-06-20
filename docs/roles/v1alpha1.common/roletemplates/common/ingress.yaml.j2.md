



# ingress.yaml.j2

---
```

# {{ name }} ingress
---
kind: Ingress
apiVersion: networking.k8s.io/v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if ingress_spec != false %}
spec:
  {{ ingress_spec | indent(width=2) }}
{% endif %}

```
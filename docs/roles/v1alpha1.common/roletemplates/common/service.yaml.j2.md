



# service.yaml.j2

---
```

# {{ name }} service
---
kind: Service
apiVersion: v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if service_spec != false %}
spec:
  {{ service_spec | indent(width=2) }}
{% endif %}

```
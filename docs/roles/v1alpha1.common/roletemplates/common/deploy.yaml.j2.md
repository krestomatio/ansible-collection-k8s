



# deploy.yaml.j2

---
```

# {{ name }} deployment
---
kind: Deployment
apiVersion: apps/v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if deploy_spec != false %}
spec:
  {{ deploy_spec | indent(width=2) }}
{% endif %}

```
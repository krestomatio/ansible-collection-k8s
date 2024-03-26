



# route.yaml.j2
  
---  
```

# {{ name }} route
---
kind: Route
apiVersion: v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if route_spec != false %}
spec:
  {{ route_spec | indent(width=2) }}
{% endif %}
  
```
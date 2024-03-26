



# cm.yaml.j2
  
---  
```

# {{ name }} configmap
---
kind: ConfigMap
apiVersion: v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if cm_data != false %}
data:
  {{ cm_data | indent(width=2) }}
{% endif %}
  
```
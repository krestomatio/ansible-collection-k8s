



# nginx.yaml.j2
  
---  
```

# {{ name }} nginx
---
kind: Nginx
apiVersion: "{{ cr_api_version }}"
{% include common_path + '/metadata.j2' ignore missing %}
{% if nginx_spec != false %}
spec:
  {{ nginx_spec | indent(width=2) }}
{% endif %}
  
```
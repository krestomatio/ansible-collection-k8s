



# php-fpm.yaml.j2
  
---  
```

# {{ name }} php-fpm
---
kind: Phpfpm
apiVersion: "{{ cr_api_version }}"
{% include common_path + '/metadata.j2' ignore missing %}
{% if php_fpm_spec != false %}
spec:
  {{ php_fpm_spec | indent(width=2) }}
{% endif %}
  
```
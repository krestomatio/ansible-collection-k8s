



# secret.yaml.j2

---
```

# {{ name }} secret
---
kind: Secret
apiVersion: v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if secret_type | default(false) != false %}
    type: '{{ secret_type }}'
{% endif %}
{% if secret_data | default(false) != false %}
data:
  {{ secret_data | indent(width=2) }}
{% endif %}
{% if secret_string_data | default(false) != false %}
stringData:
  {{ secret_string_data | indent(width=2) }}
{% endif %}

```
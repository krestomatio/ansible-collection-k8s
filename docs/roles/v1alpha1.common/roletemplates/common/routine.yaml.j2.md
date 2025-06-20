



# routine.yaml.j2

---
```

# {{ name }} routine
---
kind: Routine
apiVersion: "{{ cr_api_version }}"
{% include common_path + '/metadata.j2' ignore missing %}
{% if routine_spec != false %}
spec:
  {{ routine_spec | indent(width=2) }}
{% endif %}

```




# cronjob.yaml.j2

---
```

# {{ name }} cronjob
---
kind: CronJob
apiVersion: batch/v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if cronjob_spec != false %}
spec:
  {{ cronjob_spec | indent(width=2) }}
{% endif %}

```
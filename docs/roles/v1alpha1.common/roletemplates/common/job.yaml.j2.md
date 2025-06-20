



# job.yaml.j2

---
```

# {{ name }} job
---
kind: Job
apiVersion: batch/v1
{% include common_path + '/metadata.j2' ignore missing %}
{% if job_spec != false %}
spec:
  {{ job_spec | indent(width=2) }}
{% endif %}

```
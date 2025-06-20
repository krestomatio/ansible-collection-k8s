



# hpa.yaml.j2

---
```

# {{ name }} horizontalpodautoscaler
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
{% include common_path + '/metadata.j2' ignore missing %}
{% if hpa_spec != false %}
spec:
  scaleTargetRef:
    apiVersion: {{ hpa_ref_api_version }}
    kind: {{ hpa_ref_kind }}
    name: {{ hpa_ref_name }}
  {{ hpa_spec | indent(width=2) }}
{% endif %}

```
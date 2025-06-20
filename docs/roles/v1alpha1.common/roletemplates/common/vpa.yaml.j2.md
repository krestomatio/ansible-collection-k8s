



# vpa.yaml.j2

---
```

# {{ name }} horizontalpodautoscaler
---
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
{% include common_path + '/metadata.j2' ignore missing %}
{% if vpa_spec != false %}
spec:
  targetRef:
    apiVersion: {{ vpa_ref_api_version }}
    kind: {{ vpa_ref_kind }}
    name: {{ vpa_ref_name }}
  {{ vpa_spec | indent(width=2) }}
{% endif %}

```




# new-instance.yml


* No description available for this task - here is the definition:
```

include_tasks: condition/instantiated/not-instantiated.yml

```

* No description available for this task - here is the definition:
```

include_tasks: resource/job-new-instance.yml

```

* No description available for this task - here is the definition:
```

include_tasks: '{{ common_path }}/wait/job.yml'
vars:
  wait_job_conditions: '{{ k8s_moodle_new_instance_job.result.status.conditions |
    default([]) }}'
  wait_job_name: '{{ moodle_new_instance_job }}'

```

* No description available for this task - here is the definition:
```

include_tasks: condition/instantiated/instantiated.yml

```
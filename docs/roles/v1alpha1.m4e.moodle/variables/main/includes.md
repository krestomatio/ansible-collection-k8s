



# includes.yml

---
## moodle_not_created_needed

```

'{{ not (cr_status_properties is defined and cr_status_properties) }}'

```
## moodle_predeploy_needed

```

'{{ not moodle_status_created | bool and moodle_new_instance_job_needed | bool }}'

```
## moodle_new_instance_job_needed

```

'{{ true if ((moodle_new_instance | bool) and not (cr_status_properties.instantiated
  | default(''False'') | bool)) else false }}'

```
## moodle_update_job_needed

```

'{{ true if not moodle_status_uptodate and moodle_status_version.pendingType | default(''Other'')
  in moodle_update_allow_pending_types else false }}'

```
## moodle_not_uptodate_end_needed

```

'{{ not moodle_status_uptodate }}'

```
## moodle_pvc_data_needed

```

'{{ false if moodle_nfs_meta_name else true }}'

```
## moodle_cronjob_vpa_needed

```

'{{ moodle_cronjob_vpa_spec is defined and moodle_cronjob_vpa_spec }}'

```
## moodle_setting_up_needed

```

'{{ not moodle_not_created_needed | bool and not moodle_new_instance_job_needed |
  bool and moodle_status_setting_up | bool }}'

```
## moodle_successfull_status_needed

```

'{{ moodle_status_successful | bool }}'

```
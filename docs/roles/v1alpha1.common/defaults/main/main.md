



# main.yml
  
---
## state
  
```

present
...
  
```
## image_pull_secret
  
```

false
...
  
```
## inventory_include
  
```

false
...
  
```
## inventory_uuid
  
```

'{{ (cr_group + cr_version + cr_kind + meta_namespace + meta_name) | to_uuid }}'
  
```
## inventory_annotation_hostvars
  
```

ansible_python_interpreter: /usr/libexec/platform-python
ansible_remote_tmp: /var/tmp/.ansible
ansible_ssh_pipelining: true
  
```
## routine_k8s_status_api_version
  
```

'{{ cr_api_version }}'
  
```
## routine_k8s_status_kind
  
```

'{{ cr_kind }}'
  
```
## routine_k8s_status_name
  
```

'{{ meta_name }}'
  
```
## routine_k8s_status_namespace
  
```

'{{ meta_namespace }}'
  
```
## routine_pods_ready_group
  
```

'{{ pods_ready_group }}'
  
```
## routine_status_cr_notify
  
```

false
...
  
```
## routine_status_cr_notify_force
  
```

false
...
  
```
## routine_pvc_autoexpand_info_name
  
```

{}
  
```
## routine_pvc_autoexpand_info_keyname
  
```

pvc
...
  
```
## routine_pvc_autoexpand_info_pods_ready_group
  
```

'{{ pods_ready_group }}'
  
```
## routine_reconcile_trigger_cr_version
  
```

'{{ cr_version }}'
  
```
## routine_reconcile_trigger_cr_group
  
```

'{{ cr_group }}'
  
```
## routine_reconcile_trigger_cr_kind
  
```

'{{ cr_kind }}'
  
```
## routine_reconcile_trigger_cr_name
  
```

'{{ meta_name }}'
  
```
## routine_reconcile_trigger_cr_namespace
  
```

'{{ meta_namespace }}'
  
```
## condition_expand_keyname
  
```

'{{ routine_pvc_autoexpand_info_keyname | capitalize }}'
  
```
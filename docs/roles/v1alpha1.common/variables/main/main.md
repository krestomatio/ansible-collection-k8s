



# main.yml

---
## cr_version

```

v1alpha1
...

```
## cr_api_version

```

'{{ cr_group }}/{{ cr_version }}'

```
## cr_object

```

'{{ lookup(''vars'', cr_object_var_name, default='''') if cr_object_var_name | default(false,
  true) else '''' }}'

```
## cr_object_var_name

```

'{{ (''_'' + cr_group + ''_'' + cr_kind) | default('''') | lower | regex_replace(cr_object_var_name_regex_replace,''_'')
  if cr_group is defined and cr_kind is defined else '''' }}'

```
## cr_object_var_name_regex_replace

```

(\.|\-)
...

```
## cr_uid

```

'{{ cr_object.metadata.uid | default('''', true) }}'

```
## cr_status

```

'{{ routine_k8s_status_task.result.status | default(cr_object.status,true) | default({},true)
  }}'

```
## cr_status_ready

```

'{{ cr_status_properties.ready | default(false) | bool }}'

```
## cr_status_conditions

```

'{{ cr_status.conditions | default([]) }}'

```
## cr_status_generation

```

'{{ cr_object.metadata.generation | default(1, true) | int }}'

```
## cr_status_observed_generation

```

'{{ cr_status_properties.observedGeneration | default(0, true) | int }}'

```
## cr_status_properties

```

'{% set copy=cr_status.copy() %}{% if copy.conditions is defined %}{% set removed=copy.pop(''conditions'')
  %}{% endif %}{{ copy }}'

```
## cr_cwd

```

'{{ ''/tmp/ansible-operator/runner/'' + ''/''.join([cr_group, cr_version, cr_kind,
  meta_namespace, meta_name, ''project'']) }}'

```
## meta_name

```

'{{ ansible_operator_meta.name }}'

```
## meta_namespace

```

'{{ ansible_operator_meta.namespace }}'

```
## pods_group

```

'{{ cr_kind }}__{{ meta_namespace.replace(''-'', ''_'') }}__{{ meta_name.replace(''-'',
  ''_'') }}__pods'

```
## pods_ready_group

```

'{{ pods_group }}_ready'

```
## meta_name_max_length

```

63
...

```
## common_path

```

common
...

```
## meta_app_part_of

```

'{{ meta_name }}'

```
## meta_app_connects_to

```

connects-to.krestomat.io
...

```
## deploy_template

```

'{{ common_path }}/deploy.yaml.j2'

```
## sts_template

```

'{{ common_path }}/sts.yaml.j2'

```
## job_template

```

'{{ common_path }}/job.yaml.j2'

```
## cronjob_template

```

'{{ common_path }}/cronjob.yaml.j2'

```
## cm_template

```

'{{ common_path }}/cm.yaml.j2'

```
## pvc_template

```

'{{ common_path }}/pvc.yaml.j2'

```
## netpol_template

```

'{{ common_path }}/netpol.yaml.j2'

```
## vct_template

```

'{{ common_path }}/vct.yaml.j2'

```
## secret_template

```

'{{ common_path }}/secret.yaml.j2'

```
## service_template

```

'{{ common_path }}/service.yaml.j2'

```
## route_template

```

'{{ common_path }}/route.yaml.j2'

```
## nginx_template

```

'{{ common_path }}/nginx.yaml.j2'

```
## php_fpm_template

```

'{{ common_path }}/php-fpm.yaml.j2'

```
## ingress_template

```

'{{ common_path }}/ingress.yaml.j2'

```
## sc_template

```

'{{ common_path }}/sc.yaml.j2'

```
## routine_template

```

'{{ common_path }}/routine.yaml.j2'

```
## hpa_template

```

'{{ common_path }}/hpa.yaml.j2'

```
## vpa_template

```

'{{ common_path }}/vpa.yaml.j2'

```
## inventory_refresh_task

```

not-refresh
...

```
## inventory_annotation_extra_cr_cwd

```

'krestomat.io/inventory-extra-cr-cwd: ''{{ cr_cwd }}''

  '

```
## k8s_api_resources

```

'{{ (lookup(''pipe'',''kubectl api-resources --output=name --cached='' + api_resources_cached
  | default(true) | string + '' 2> /dev/null || echo "api_resources_exit_code: $?"'')
  | default('''')).split(''

  '') }}'

```
## k8s_distribution

```

'{{ ''okd'' if ''clusterversions.config.openshift.io'' in k8s_api_resources else ''k8s''
  }}'

```




# status.yml
  
---
## moodle_status_version
  
```

'{{ cr_status_properties.version | default({},true) }}'
  
```
## moodle_status_uptodate
  
```

'{{ cr_status_properties.upToDate | default(''True'') | bool }}'
  
```
## moodle_status_created
  
```

'{{ (cr_status_properties.created | default(''False'') | bool) }}'
  
```
## moodle_status_setting_up
  
```

'{{ true if lookup(''template'', moodle_config_template) | sha1 != cr_status.configHash
  | default('''') else false }}'
  
```
## moodle_status_successful
  
```

'{{ not moodle_status_setting_up }}'
  
```
## moodle_status_script_version
  
```

true
...
  
```
## moodle_status_script_usage
  
```

true
...
  
```
## moodle_status_script
  
```

'{{ moodle_scripts_path }}/status.php {{ ''-ch -l'' + ('' -v'' if moodle_status_script_version
  else '''') + ('' -u'' if moodle_status_script_usage else '''') + ('' -c='' + moodle_status_script_checks
  if moodle_status_script_checks is defined and moodle_status_script_checks else '''')
  }}'
  
```
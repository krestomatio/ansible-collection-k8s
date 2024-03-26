



# customresources.yml
  
---
## moodle_php_fpm
  
```

'{{ moodle_appname }}-php-fpm'
  
```
## moodle_php_fpm_spec
  
```

"cr_state: {{ php_fpm_cr_state | default(cr_state) }}\n{%  if common_labels | default(false)\
  \ %}\ncommon_labels: |-\n  {{ common_labels | indent(2) }}\n{% endif %}\n{% for\
  \ _php_fpm_varname in query('varnames', '^php_fpm.+')  %}\n{% if _php_fpm_varname\
  \ is not match('php_fpm_spec') and _php_fpm_varname is not regex('.*_task$') %}\n\
  {% set _php_fpm_vartype = lookup('vars', _php_fpm_varname) | type_debug %}\n{% set\
  \ _php_fpm_varvalue = lookup('vars', _php_fpm_varname) %}\n{% if _php_fpm_vartype\
  \ == 'bool' %}\n{{ _php_fpm_varname }}: {{ _php_fpm_varvalue }}\n{% elif _php_fpm_vartype\
  \ == 'list' or _php_fpm_vartype == 'dict'  %}\n{{ _php_fpm_varname }}:\n  {{ _php_fpm_varvalue\
  \ | to_nice_yaml(indent=2) | indent(2) -}}\n{% elif _php_fpm_varvalue is regex('\\\
  n|\\t') %}\n{{ _php_fpm_varname }}: |\n  {{ _php_fpm_varvalue | indent(2) }}\n{%\
  \ else %}\n{{ _php_fpm_varname }}: '{{ _php_fpm_varvalue | regex_replace(\"'\",\
  \ \"''\") }}'\n{% endif %}\n{% endif %}\n{% endfor %}"
  
```
## moodle_nginx
  
```

'{{ moodle_appname }}-nginx'
  
```
## moodle_nginx_spec
  
```

"cr_state: {{ nginx_cr_state | default(cr_state) }}\n{%  if common_labels | default(false)\
  \ %}\ncommon_labels: |-\n  {{ common_labels | indent(2) }}\n{% endif %}\n{% for\
  \ _nginx_varname in query('varnames', '^nginx.+')  %}\n{% if _nginx_varname is not\
  \ match('nginx_spec') and _nginx_varname is not regex('.*_task$') %}\n{% set _nginx_vartype\
  \ = lookup('vars', _nginx_varname) | type_debug %}\n{% set _nginx_varvalue = lookup('vars',\
  \ _nginx_varname) %}\n{% if _nginx_vartype == 'bool' %}\n{{ _nginx_varname }}: {{\
  \ _nginx_varvalue }}\n{% elif _nginx_vartype == 'list' or _nginx_vartype == 'dict'\
  \  %}\n{{ _nginx_varname }}:\n  {{ _nginx_varvalue | to_nice_yaml(indent=2) | indent(2)\
  \ -}}\n{% elif _nginx_varvalue is regex('\\n|\\t') %}\n{{ _nginx_varname }}: |\n\
  \  {{ _nginx_varvalue | indent(2) }}\n{% else %}\n{{ _nginx_varname }}: '{{ _nginx_varvalue\
  \ | regex_replace(\"'\", \"''\") }}'\n{% endif %}\n{% endif %}\n{% endfor %}"
  
```
## moodle_routine
  
```

'{{ moodle_appname }}-routine'
  
```
## moodle_routine_spec
  
```

"{%  if common_labels | default(false) %}\ncommon_labels: |-\n  {{ common_labels |\
  \ indent(2) }}\n{% endif %}\n{% for _routine_varname in query('varnames', '^routine.+')\
  \  %}\n{% if _routine_varname is not match('routine_spec') and _routine_varname\
  \ is not regex('.*_task$') %}\n{% set _routine_vartype = lookup('vars', _routine_varname)\
  \ | type_debug %}\n{% set _routine_varvalue = lookup('vars', _routine_varname) %}\n\
  {% if _routine_vartype == 'bool' %}\n{{ _routine_varname }}: {{ _routine_varvalue\
  \ }}\n{% elif _routine_vartype == 'list' or _routine_vartype == 'dict'  %}\n{{ _routine_varname\
  \ }}:\n  {{ _routine_varvalue | to_nice_yaml(indent=2) | indent(2) -}}\n{% elif\
  \ _routine_varvalue is regex('\\n|\\t') %}\n{{ _routine_varname }}: |\n  {{ _routine_varvalue\
  \ | indent(2) }}\n{% else %}\n{{ _routine_varname }}: '{{ _routine_varvalue | regex_replace(\"\
  '\", \"''\") }}'\n{% endif %}\n{% endif %}\n{% endfor %}"
  
```
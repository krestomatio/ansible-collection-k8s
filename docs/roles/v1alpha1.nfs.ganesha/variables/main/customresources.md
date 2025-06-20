



# customresources.yml

---
## ganesha_routine

```

'{{ ganesha_appname }}-routine'

```
## ganesha_routine_spec

```

"{% for _routine_varname in query('varnames', '^routine.+')  %}\n{% if _routine_varname\
  \ is not match('routine_spec') and _routine_varname is not regex('.*_task$') %}\n\
  {% set _routine_vartype = lookup('vars', _routine_varname) | type_debug %}\n{% set\
  \ _routine_varvalue = lookup('vars', _routine_varname) %}\n{% if _routine_vartype\
  \ == 'bool' %}\n{{ _routine_varname }}: {{ _routine_varvalue }}\n{% elif _routine_vartype\
  \ == 'list' or _routine_vartype == 'dict'  %}\n{{ _routine_varname }}:\n  {{ _routine_varvalue\
  \ | to_nice_yaml(indent=2) | indent(2) -}}\n{% elif _routine_varvalue is regex('\\\
  n|\\t') %}\n{{ _routine_varname }}: |\n  {{ _routine_varvalue | indent(2) }}\n{%\
  \ else %}\n{{ _routine_varname }}: '{{ _routine_varvalue | regex_replace(\"'\",\
  \ \"''\") }}'\n{% endif %}\n{% endif %}\n{% endfor %}"

```
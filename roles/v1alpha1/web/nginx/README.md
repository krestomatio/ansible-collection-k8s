Role Name
=========

Role to handle Nginx with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`defaults/main/main.yml`](defaults/main/main.yml)
- See [`defaults/main/nginx.yml`](defaults/main/postgres.yml)

Dependencies
------------

collections:
- kubernetes.core
- operator_sdk.util

Example Playbook
----------------

```yaml
- hosts: localhost
  gather_facts: no
  collections:
    - kubernetes.core
    - operator_sdk.util
  tasks:
    - import_role:
        name: "nginx"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

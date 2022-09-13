Role Name
=========

Role to handle Moodle with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`defaults/main/main.yml`](defaults/main/main.yml)
- See [`defaults/main/moodle.yml`](defaults/main/moodle.yml)
- See [`defaults/main/php-fpm.yml`](defaults/main/php-fpm.yml)
- See [`defaults/main/nginx.yml`](../../web/nginx/defaults/main/nginx.yml)
- See [`vars/main/nginx.yml`](vars/main/nginx.yml)

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
        name: "krestomatio.k8s.v1alpha1.m4e.moodle"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

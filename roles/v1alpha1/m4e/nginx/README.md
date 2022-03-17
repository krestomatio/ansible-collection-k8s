Role Name
=========

Role to handle Nginx for Moodle with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`vars/main/main.yml`](vars/main/main.yml)
- See [`vars/main/nginx.yml`](vars/main/nginx.yml)
- See [`defaults/main/nginx.yml`](../../web/nginx/defaults/main/nginx.yml)

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
        name: "krestomatio.k8s.v1alpha1.m4e.nginx"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

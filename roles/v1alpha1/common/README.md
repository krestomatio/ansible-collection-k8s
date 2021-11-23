Role Name
=========

Role to handle common tasks with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`defaults/main/main.yml`](defaults/main/main.yml)

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
        name: "krestomatio.k8s.common"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

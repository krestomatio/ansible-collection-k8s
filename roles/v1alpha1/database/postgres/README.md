Role Name
=========

Role to handle Postgres with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`defaults/main/main.yml`](defaults/main/main.yml)
- See [`defaults/main/postgres.yml`](defaults/main/postgres.yml)

Dependencies
------------

collections:
- operator_sdk.util
- community.kubernetes

Example Playbook
----------------

```yaml
- hosts: localhost
  gather_facts: no
  collections:
    - community.kubernetes
    - operator_sdk.util
  tasks:
    - import_role:
        name: "postgres"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

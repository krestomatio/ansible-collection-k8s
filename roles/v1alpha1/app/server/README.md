Role Name
=========

Role to handle a Handler Server for Graphql Engine with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`defaults/main/main.yml`](defaults/main/main.yml)
- See [`defaults/main/server.yml`](defaults/main/server.yml)
- See [`defaults/main/postgres.yml`](../../database/postgres/defaults/main/postgres.yml)
- See [`vars/main/postgres.yml`](vars/main/postgres.yml)

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
        name: "g12e"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

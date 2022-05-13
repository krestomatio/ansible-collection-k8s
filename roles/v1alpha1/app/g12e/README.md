Role Name
=========

Role to handle Graphql Engine with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`defaults/main/main.yml`](defaults/main/main.yml)
- See [`defaults/main/graphql-engine.yml`](defaults/main/graphql-engine.yml)
- See [`defaults/main/postgres.yml`](../../database/postgres/defaults/main/postgres.yml)
- See [`vars/main/postgres.yml`](vars/main/postgres.yml)

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
        name: "krestomatio.k8s.v1alpha1.app.g12e"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

Role Name
=========

Role to allocate nfs servers for RWX using Ansible Operator SDK and rook nfs

Requirements
------------

None

Role Variables
--------------

- See [`defaults/main.yml`](defaults/main.yml)
- See [`defaults/moodle.yml`](defaults/server.yml)

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
        name: krestomatio.k8s.server
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

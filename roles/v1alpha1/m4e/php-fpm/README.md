Role Name
=========

Role to handle PHP-FPM for Moodle with Ansible Operator SDK

Requirements
------------

None

Role Variables
--------------

- See [`vars/main/main.yml`](vars/main/main.yml)
- See [`vars/main/php-fpm.yml`](vars/main/php-fpm.yml)
- See [`defaults/main/php-fpm.yml`](../../web/php-fpm/defaults/main/php-fpm.yml)

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
        name: "krestomatio.k8s.v1alpha1.m4e.php-fpm"
```
License
-------

Apache 2.0

Author Information
------------------

Job Céspedes Ortiz: jobcespedes@krestomatio.com

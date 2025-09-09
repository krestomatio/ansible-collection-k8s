# Ansible Collection: krestomatio.k8s

Collection version 0.4.38

> * [Description](#description)
> * [Plugin Index](#plugin-index)

## Description

To use in conjunction with kubernetes and operator sdk

**Author:**

* Job Céspedes Ortiz \<jobcespedes@krestomatio.com\>

**Supported ansible-core versions:**

* 2.18.0 or newer

### Collection links

* [Issue Tracker](https://github.com/krestomatio/ansible-collection-k8s/issues)
* [Homepage](https://krestomat.io)
* [Repository (Sources)](https://github.com/krestomatio/ansible-collection-k8s)

## Plugin Index

These are the plugins in the krestomatio.k8s collection:

### Roles

* [v1alpha1.app.g12e](roles/v1alpha1.app.g12e/index.md)
* [v1alpha1.app.server](roles/v1alpha1.app.server/index.md)
* [v1alpha1.common](roles/v1alpha1.common/index.md)
* [v1alpha1.database.keydb](roles/v1alpha1.database.keydb/index.md)
* [v1alpha1.database.postgres](roles/v1alpha1.database.postgres/index.md)
* [v1alpha1.m4e.moodle](roles/v1alpha1.m4e.moodle/index.md)
* [v1alpha1.m4e.nginx](roles/v1alpha1.m4e.nginx/index.md)
* [v1alpha1.m4e.php_fpm](roles/v1alpha1.m4e.php_fpm/index.md)
* [v1alpha1.m4e.routine](roles/v1alpha1.m4e.routine/index.md)
* [v1alpha1.nfs.ganesha](roles/v1alpha1.nfs.ganesha/index.md)
* [v1alpha1.nfs.routine](roles/v1alpha1.nfs.routine/index.md)
* [v1alpha1.web.nginx](roles/v1alpha1.web.nginx/index.md)
* [v1alpha1.web.php_fpm](roles/v1alpha1.web.php_fpm/index.md)

### Modules

* [k8s_status](modules/k8s_status.md)
* [mount_info](modules/mount_info.md)
* [pvc_autoexpand_info](modules/pvc_autoexpand_info.md)

### Filter Plugins

* [autoexpand_size_gib](filters/autoexpand_size_gib.md)
* [b_to_gib](filters/b_to_gib.md)

### Inventory Plugins

* [inventory](inventories/inventory.md)

### Test Plugins

* [below_twenty_pct](tests/below_twenty_pct.md)

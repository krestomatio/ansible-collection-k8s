## Changes

### New Features

* add option to set export ownership/permissions (Job Céspedes Ortiz)
* add option for init server pvc size (Job Céspedes Ortiz)
* use pvc info for autoexpansion in nfs server (Job Céspedes Ortiz)
* add python code related to autoexpansion (Job Céspedes Ortiz)
* add filter to convert to gb (Job Céspedes Ortiz)
* nfs: add option to modify servers namespace (Job Céspedes Ortiz)
* nfs: add mount info to status (Job Céspedes Ortiz)
* add nfs server role (Job Céspedes Ortiz)
* add m4e role (Job Céspedes Ortiz)
* add common role (Job Céspedes Ortiz)
* inventory: add k8s inventory plugin (Job Céspedes Ortiz)

### Bug Fixes

* omit pvc info when state absent (Job Céspedes Ortiz)
* nfs: wait for sts after adding labels (Job Céspedes Ortiz)
* nfs: adjust refresh inventory condition (Job Céspedes Ortiz)
* set part of and create by labels conditionally (Job Céspedes Ortiz)
* fix metadadata idempotency (Job Céspedes Ortiz)

### Code Refactoring

* clean up internal doc and default valur for server_sc_allow_volume_expansion (Job Céspedes Ortiz)
* move rescue as a common task (Job Céspedes Ortiz)
* plugins: rename pvc_info (Job Céspedes Ortiz)
* add ready fact (Job Céspedes Ortiz)
* change GB to GiB (Job Céspedes Ortiz)
* adjust status properties (Job Céspedes Ortiz)
* move refresh inventory task to common role (Job Céspedes Ortiz)
* use NFSServer CR (Job Céspedes Ortiz)
* change configmap name (Job Céspedes Ortiz)
* organize m4e tasks (Job Céspedes Ortiz)
* move M4e kind into m4e group (Job Céspedes Ortiz)
* change status var name (Job Céspedes Ortiz)

### Documentation

* add galaxy info and license (Job Céspedes Ortiz)

### Chores

* add sts template (Job Céspedes Ortiz)

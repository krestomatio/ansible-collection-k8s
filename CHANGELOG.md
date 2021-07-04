## Changes

### New Features

* add ansible lint (Job Céspedes Ortiz)
* add option to set export ownership/permissions (Job Céspedes Ortiz)
* add option for init server pvc size (Job Céspedes Ortiz)
* use pvc info for autoexpansion in nfs server (Job Céspedes Ortiz)

### Bug Fixes

* add condition to pvc info (Job Céspedes Ortiz)
* omit pvc info when state absent (Job Céspedes Ortiz)

### Code Refactoring

* plugins: remove unused import (Job Céspedes Ortiz)
* clean up internal doc and default valur for server_sc_allow_volume_expansion (Job Céspedes Ortiz)
* move rescue as a common task (Job Céspedes Ortiz)
* plugins: rename pvc_info (Job Céspedes Ortiz)

### Documentation

* update README (Job Céspedes Ortiz)

### Chores

* release: 0.0.2 (krestomatio-cibot)

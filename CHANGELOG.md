## Changes

### New Features

* replace list in status (Job Céspedes Ortiz)
* m4e: use randomly generated credentials for postgres db (Job Céspedes Ortiz)
* do not log secret resources (Job Céspedes Ortiz)
* m4e: renew admin user password using bcrypt compatible hash (Job Céspedes Ortiz)
* add assertions (Job Céspedes Ortiz)

### Bug Fixes

* plugins: add workaround to check if a condition has transition or not (Job Céspedes Ortiz)
* plugins: add workaround to completely replace lists (Job Céspedes Ortiz)
* plugins: add workaround for k8s status to ignore arg with none (Job Céspedes Ortiz)
* plugins: remove dependencies for workaround of k8s status (Job Céspedes Ortiz)
* plugins: add workaround for k8s status (Job Céspedes Ortiz)
* m4e: do not attempt reset pass task during removal (Job Céspedes Ortiz)

### Code Refactoring

* m4e: handle already instantiated db as a warning (Job Céspedes Ortiz)

### Chores

* add dependencies (Job Céspedes Ortiz)
* release: 0.0.28 (krestomatio-cibot)

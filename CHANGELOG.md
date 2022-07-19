## Changes

### New Features

* common: add resource wait tasks (Job Céspedes Ortiz)
* m4e: do not run certain status logic when moodle upgrade is running (Job Céspedes Ortiz)
* add k8s api resources list (Job Céspedes Ortiz)
* add wait job task (Job Céspedes Ortiz)

### Code Refactoring

* do not wait on finalizer by default (Job Céspedes Ortiz)
* postgres: limit resource removal included in finalizer to necessary ones (Job Céspedes Ortiz)
* keydb: limit resource removal included in finalizer to necessary ones (Job Céspedes Ortiz)
* m4e: limit resource removal included in finalizer to necessary ones (Job Céspedes Ortiz)
* web: limit resource removal included in finalizer to necessary ones (Job Céspedes Ortiz)
* nfs: limit resource removal included in finalizer to necessary ones (Job Céspedes Ortiz)

### Chores

* release: 0.1.18 (Job Céspedes Ortiz)

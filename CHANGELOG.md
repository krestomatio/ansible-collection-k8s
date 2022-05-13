## Changes

### New Features

* add php ini and config to job, cronjob (Job Céspedes Ortiz)
* m4e: add php extra config to jobs and cronjob (Job Céspedes Ortiz)
* postgres: add service status reference (Job Céspedes Ortiz)
* keydb: add service status reference (Job Céspedes Ortiz)
* nfs: use sts and nfs ganesha image (Job Céspedes Ortiz)
* m4e: add optional nfs volume (Job Céspedes Ortiz)

### Bug Fixes

* m4e: add condition to nginx and php-fpm predeploy (Job Céspedes Ortiz)
* m4e: change var names to ref other dependant cr (Job Céspedes Ortiz)
* m4e: set source for nginx pvc (Job Céspedes Ortiz)
* postgres: rename pgbouncer secret key (Job Céspedes Ortiz)

### Code Refactoring

* apply linting (Job Céspedes Ortiz)
* m4e: use startup probe for jobs (Job Céspedes Ortiz)
* m4e: group moodle tasks in folder (Job Céspedes Ortiz)
* avoid waiting for cr in ansible check mode (Job Céspedes Ortiz)
* nginx: add prefix to config names (Job Céspedes Ortiz)
* php-fpm: add prefix to config names (Job Céspedes Ortiz)
* nfs: update service status reference (Job Céspedes Ortiz)
* fix variable inheritance in dependent cr (Job Céspedes Ortiz)
* m4e: simply other krestomatio operators integration (Job Céspedes Ortiz)
* m4e: limit routine status uptade to parent cr (Job Céspedes Ortiz)
* move k8s status to routine dir (Job Céspedes Ortiz)
* wait for nginx resource (Job Céspedes Ortiz)
* rename inventory annotation related variables (Job Céspedes Ortiz)
* m4e: adjust role group structure (Job Céspedes Ortiz)
* m4e: change reconcile trigger and status (Job Céspedes Ortiz)
* change variable inheritance for dependant cr (Job Céspedes Ortiz)
* nginx: change templates (Job Céspedes Ortiz)
* app: change templates (Job Céspedes Ortiz)
* nginx: fix indentation (Job Céspedes Ortiz)
* postgres: fix indentation (Job Céspedes Ortiz)
* create nginx and routine roles in m4e (Job Céspedes Ortiz)
* m4e: remove postgres (Job Céspedes Ortiz)
* use one task for cleanup resources (Job Céspedes Ortiz)
* moodle: remove quote filter to use single quotes (Job Céspedes Ortiz)

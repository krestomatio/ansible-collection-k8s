## Changes

### New Features

* change default expose type based on distribution (Job Céspedes Ortiz)
* m4e: add Moodle autoupdate (Job Céspedes Ortiz)
* m4e: validate config.php when syncing (Job Céspedes Ortiz)
* common: use ansible ssh pipelining by default (Job Céspedes Ortiz)
* suspend cronjob if moodle update is pending (Job Céspedes Ortiz)
* add up-to-date condition (Job Céspedes Ortiz)
* nfs: use optional ansible inventory refresh task (Job Céspedes Ortiz)
* add optional ansible refresh inventory tasks (Job Céspedes Ortiz)
* disable moodle plugin web installation by default (Job Céspedes Ortiz)

### Code Refactoring

* m4e: reorder variables (Job Céspedes Ortiz)
* m4e: rename moodle new instance variables (Job Céspedes Ortiz)
* common: change reference from expand to expansion (Job Céspedes Ortiz)
* m4e: use moodle layer instead of php-fpm (Job Céspedes Ortiz)
* m4e: revert option to copy moodle app to emptydir (Job Céspedes Ortiz)

### Chores

* m4e: bump image versions with updatebot (krestomatio-cibot)
* release: 0.0.16 (krestomatio-cibot)

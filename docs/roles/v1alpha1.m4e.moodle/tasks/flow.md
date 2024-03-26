



# Flow
  
```mermaid  
graph LR  
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)  
moodle/main.yml(moodle/main.yml) --> predeploy.yml(predeploy.yml)  
moodle/main.yml(moodle/main.yml) --> resource/secret-admin.yml(resource/secret-admin.yml)  
moodle/main.yml(moodle/main.yml) --> resource/pvc-moodledata.yml(resource/pvc-moodledata.yml)  
moodle/main.yml(moodle/main.yml) --> resource/secret-config.yml(resource/secret-config.yml)  
moodle/main.yml(moodle/main.yml) --> resource/cm-scripts.yml(resource/cm-scripts.yml)  
moodle/main.yml(moodle/main.yml) --> new-instance.yml(new-instance.yml)  
moodle/main.yml(moodle/main.yml) --> resource/php-fpm.yml(resource/php-fpm.yml)  
moodle/main.yml(moodle/main.yml) --> routine/status.yml(routine/status.yml)  
moodle/main.yml(moodle/main.yml) --> update.yml(update.yml)  
moodle/main.yml(moodle/main.yml) --> resource/nginx.yml(resource/nginx.yml)  
moodle/main.yml(moodle/main.yml) --> resource/cronjob.yml(resource/cronjob.yml)  
moodle/main.yml(moodle/main.yml) --> resource/cronjob-vpa.yml(resource/cronjob-vpa.yml)  
moodle/main.yml(moodle/main.yml) --> resource/routine.yml(resource/routine.yml)  
moodle/new-instance.yml(moodle/new-instance.yml) --> condition/instantiated/not-instantiated.yml(condition/instantiated/not-instantiated.yml)  
moodle/new-instance.yml(moodle/new-instance.yml) --> resource/job-new-instance.yml(resource/job-new-instance.yml)  
moodle/new-instance.yml(moodle/new-instance.yml) --> condition/instantiated/instantiated.yml(condition/instantiated/instantiated.yml)  
moodle/predeploy.yml(moodle/predeploy.yml) --> resource/nginx.yml(resource/nginx.yml)  
moodle/predeploy.yml(moodle/predeploy.yml) --> resource/php-fpm.yml(resource/php-fpm.yml)  
moodle/update.yml(moodle/update.yml) --> resource/cronjob.yml(resource/cronjob.yml)  
moodle/update.yml(moodle/update.yml) --> resource/routine.yml(resource/routine.yml)  
moodle/update.yml(moodle/update.yml) --> resource/job-update.yml(resource/job-update.yml)  
moodle/update.yml(moodle/update.yml) --> condition/uptodate/started.yml(condition/uptodate/started.yml)  
resource/secret-admin.yml(resource/secret-admin.yml) --> routine/reset-admin-pass.yml(routine/reset-admin-pass.yml)  
routine/status.yml(routine/status.yml) --> condition/uptodate//{{ routine_status_moodle_version_condition }}.yml(condition/uptodate//{{ routine_status_moodle_version_condition }}.yml)  
```
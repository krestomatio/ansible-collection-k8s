



# update.yml


* suspend cronjob

* omit version during routine status update

* create update job

* No description available for this task - here is the definition:  
```

include_tasks: condition/uptodate/started.yml
  
```

* end play, complete update job will trigger new reconcile
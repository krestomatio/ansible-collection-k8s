



# job.yml


* Block: wait job

    * check kind: Job, name: {{ wait_job_name }}

    * end play and wait new reconcile for kind: job, name: {{ wait_job_name }}
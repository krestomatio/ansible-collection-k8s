



# resource.yml


* Block: wait resource

    * check kind: {{ wait_resource_kind }}, name: {{ wait_resource_name }}

    * end play and wait new reconcile for kind: {{ wait_resource_kind }}, name: {{ wait_resource_name }}
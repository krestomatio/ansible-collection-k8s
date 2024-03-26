



# Flow
  
```mermaid  
graph LR  
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)  
nginx.yml(nginx.yml) --> resource/{{ nginx_ingress_type }}.yml(resource/{{ nginx_ingress_type }}.yml)  
state/absent/nginx.yml(state/absent/nginx.yml) --> resource/{{ nginx_ingress_type }}.yml(resource/{{ nginx_ingress_type }}.yml)  
state/absent/nginx.yml(state/absent/nginx.yml) --> resource/deploy.yml(resource/deploy.yml)  
```
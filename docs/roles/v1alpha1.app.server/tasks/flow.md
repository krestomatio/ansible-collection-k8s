



# Flow

```mermaid
graph LR
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)
server.yml(server.yml) --> resource/deploy.yml(resource/deploy.yml)
server.yml(server.yml) --> resource/service.yml(resource/service.yml)
server.yml(server.yml) --> resource/{{ server_ingress_type }}.yml(resource/{{ server_ingress_type }}.yml)
state/absent/main.yml(state/absent/main.yml) --> server.yml(server.yml)
state/absent/main.yml(state/absent/main.yml) --> postgres.yml(postgres.yml)
state/absent/server.yml(state/absent/server.yml) --> resource/{{ server_ingress_type }}.yml(resource/{{ server_ingress_type }}.yml)
state/absent/server.yml(state/absent/server.yml) --> resource/service.yml(resource/service.yml)
state/absent/server.yml(state/absent/server.yml) --> resource/deploy.yml(resource/deploy.yml)
```




# Flow
  
```mermaid  
graph LR  
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)  
graphql-engine.yml(graphql-engine.yml) --> resource/secret-handler.yml(resource/secret-handler.yml)  
graphql-engine.yml(graphql-engine.yml) --> resource/deploy.yml(resource/deploy.yml)  
graphql-engine.yml(graphql-engine.yml) --> resource/service.yml(resource/service.yml)  
graphql-engine.yml(graphql-engine.yml) --> resource/{{ graphql_engine_ingress_type }}.yml(resource/{{ graphql_engine_ingress_type }}.yml)  
state/absent/graphql-engine.yml(state/absent/graphql-engine.yml) --> resource/{{ graphql_engine_ingress_type }}.yml(resource/{{ graphql_engine_ingress_type }}.yml)  
state/absent/graphql-engine.yml(state/absent/graphql-engine.yml) --> resource/service.yml(resource/service.yml)  
state/absent/graphql-engine.yml(state/absent/graphql-engine.yml) --> resource/deploy.yml(resource/deploy.yml)  
state/absent/graphql-engine.yml(state/absent/graphql-engine.yml) --> resource/secret-handler.yml(resource/secret-handler.yml)  
state/absent/main.yml(state/absent/main.yml) --> graphql-engine.yml(graphql-engine.yml)  
state/absent/main.yml(state/absent/main.yml) --> postgres.yml(postgres.yml)  
state/present/main.yml(state/present/main.yml) --> postgres.yml(postgres.yml)  
state/present/main.yml(state/present/main.yml) --> graphql-engine.yml(graphql-engine.yml)  
```
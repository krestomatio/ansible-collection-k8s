



# Flow
  
```mermaid  
graph LR  
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)  
pgbouncer-readonly.yml(pgbouncer-readonly.yml) --> resource/pgbouncer-readonly/secret.yml(resource/pgbouncer-readonly/secret.yml)  
pgbouncer-readonly.yml(pgbouncer-readonly.yml) --> resource/pgbouncer-readonly/cm.yml(resource/pgbouncer-readonly/cm.yml)  
pgbouncer-readonly.yml(pgbouncer-readonly.yml) --> resource/pgbouncer-readonly/svc.yml(resource/pgbouncer-readonly/svc.yml)  
pgbouncer-readonly.yml(pgbouncer-readonly.yml) --> resource/pgbouncer-readonly/deploy.yml(resource/pgbouncer-readonly/deploy.yml)  
pgbouncer-readonly.yml(pgbouncer-readonly.yml) --> resource/pgbouncer-readonly/vpa.yml(resource/pgbouncer-readonly/vpa.yml)  
pgbouncer.yml(pgbouncer.yml) --> resource/pgbouncer/secret.yml(resource/pgbouncer/secret.yml)  
pgbouncer.yml(pgbouncer.yml) --> resource/pgbouncer/cm.yml(resource/pgbouncer/cm.yml)  
pgbouncer.yml(pgbouncer.yml) --> resource/pgbouncer/svc.yml(resource/pgbouncer/svc.yml)  
pgbouncer.yml(pgbouncer.yml) --> resource/pgbouncer/deploy.yml(resource/pgbouncer/deploy.yml)  
pgbouncer.yml(pgbouncer.yml) --> resource/pgbouncer/vpa.yml(resource/pgbouncer/vpa.yml)  
postgres.yml(postgres.yml) --> resource/postgres/secret.yml(resource/postgres/secret.yml)  
postgres.yml(postgres.yml) --> resource/postgres/cm.yml(resource/postgres/cm.yml)  
postgres.yml(postgres.yml) --> resource/postgres/cm-vars.yml(resource/postgres/cm-vars.yml)  
postgres.yml(postgres.yml) --> resource/postgres/svc.yml(resource/postgres/svc.yml)  
postgres.yml(postgres.yml) --> resource/postgres/sts.yml(resource/postgres/sts.yml)  
postgres.yml(postgres.yml) --> resource/postgres/vpa.yml(resource/postgres/vpa.yml)  
readreplicas.yml(readreplicas.yml) --> resource/readreplicas/svc.yml(resource/readreplicas/svc.yml)  
readreplicas.yml(readreplicas.yml) --> resource/readreplicas/svc-readonly.yml(resource/readreplicas/svc-readonly.yml)  
readreplicas.yml(readreplicas.yml) --> resource/readreplicas/sts.yml(resource/readreplicas/sts.yml)  
readreplicas.yml(readreplicas.yml) --> resource/readreplicas/vpa.yml(resource/readreplicas/vpa.yml)  
```
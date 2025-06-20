



# Flow

```mermaid
graph LR
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)
keydb.yml(keydb.yml) --> resource/netpol.yml(resource/netpol.yml)
keydb.yml(keydb.yml) --> resource/secret.yml(resource/secret.yml)
keydb.yml(keydb.yml) --> resource/cm.yml(resource/cm.yml)
keydb.yml(keydb.yml) --> resource/svc-headless.yml(resource/svc-headless.yml)
keydb.yml(keydb.yml) --> resource/svc.yml(resource/svc.yml)
keydb.yml(keydb.yml) --> resource/sts.yml(resource/sts.yml)
keydb.yml(keydb.yml) --> resource/vpa.yml(resource/vpa.yml)
state/absent/keydb.yml(state/absent/keydb.yml) --> resource/sts.yml(resource/sts.yml)
```
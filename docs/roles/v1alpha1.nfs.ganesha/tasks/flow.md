



# Flow
  
```mermaid  
graph LR  
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)  
ganesha.yml(ganesha.yml) --> resource/cm.yml(resource/cm.yml)  
ganesha.yml(ganesha.yml) --> resource/svc.yml(resource/svc.yml)  
ganesha.yml(ganesha.yml) --> resource/sts.yml(resource/sts.yml)  
ganesha.yml(ganesha.yml) --> resource/vpa.yml(resource/vpa.yml)  
ganesha.yml(ganesha.yml) --> resource/sc-generated.yml(resource/sc-generated.yml)  
ganesha.yml(ganesha.yml) --> resource/routine.yml(resource/routine.yml)  
state/absent/ganesha.yml(state/absent/ganesha.yml) --> resource/routine.yml(resource/routine.yml)  
state/absent/ganesha.yml(state/absent/ganesha.yml) --> resource/sts.yml(resource/sts.yml)  
state/absent/ganesha.yml(state/absent/ganesha.yml) --> resource/sc-generated.yml(resource/sc-generated.yml)  
```
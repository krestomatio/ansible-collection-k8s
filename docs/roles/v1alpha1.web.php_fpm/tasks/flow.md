



# Flow
  
```mermaid  
graph LR  
main.yml(main.yml) --> state/{{ cr_state }}/main.yml(state/{{ cr_state }}/main.yml)  
php-fpm.yml(php-fpm.yml) --> resource/netpol.yml(resource/netpol.yml)  
php-fpm.yml(php-fpm.yml) --> resource/cm.yml(resource/cm.yml)  
php-fpm.yml(php-fpm.yml) --> resource/deploy.yml(resource/deploy.yml)  
php-fpm.yml(php-fpm.yml) --> resource/hpa.yml(resource/hpa.yml)  
php-fpm.yml(php-fpm.yml) --> resource/vpa.yml(resource/vpa.yml)  
php-fpm.yml(php-fpm.yml) --> resource/service.yml(resource/service.yml)  
state/absent/php-fpm.yml(state/absent/php-fpm.yml) --> resource/deploy.yml(resource/deploy.yml)  
```
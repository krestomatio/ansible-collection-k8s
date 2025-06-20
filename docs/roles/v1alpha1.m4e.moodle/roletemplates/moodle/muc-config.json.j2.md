



# muc-config.json.j2

---
```

{
    "stores": {
{% if moodle_redis_muc_config %}
        "redis": {
            "type": "redis",
            "config": {
                "server": "{{ moodle_redis_host }}",
                "prefix": "{{ moodle_redis_muc_config_prefix }}",
                "password": "{{ moodle_redis_password }}",
                "serializer": {{ moodle_redis_muc_config_serializer }},
                "compressor": {{ moodle_redis_muc_config_compressor }}
            }
        },
{% endif %}
{% if moodle_local_dir is defined and moodle_local_dir %}
        "local": {
            "type": "file",
            "config": {
                "path": "{{ moodle_local_dir }}/cache-local",
                "autocreate": 1
            }
        },
{% endif %}
        "shared": {
            "type": "file",
            "config": {
                "path": "{{ moodle_volume_moodledata.mount_path }}/cache-shared",
                "autocreate": 1
            }
        }
    },
    "rules": {
        "application": [
            {
                "conditions": {
                    "canuselocalstore": true
                },
                "stores": [
{% if moodle_local_dir is defined and moodle_local_dir %}
                    "local",
{% endif %}
{% if moodle_redis_muc_config %}
                    "redis",
{% endif %}
                    "shared"
                ]
            },
            {
                "stores": [
{% if moodle_redis_muc_config %}
                    "redis",
{% endif %}
                    "shared"
                ]
            }
        ],
        "session": [
            {
                "stores": [
{% if moodle_redis_muc_config %}
                    "redis",
{% endif %}
                    "shared"
                ]
            }
        ],
        "request": []
    }
}

```




# multimaster.yml

---
## keydb_size

```

3
...

```
## keydb_args

```

- --masterauth "$(KEYDB_PASSWORD)"
- --requirepass "$(KEYDB_PASSWORD)"

```
## keydb_mode_config

```

'multi-master yes

  active-replica yes

  '

```
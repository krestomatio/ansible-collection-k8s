# autoexpand_size_gib
Autoexpand size in GiB

## Synopsis

Get autoexpand size in GiB




## Parameters

  _input (True, float, None)
    Size total GiB



## Examples

```yaml
    
      autoexpand_size_gib: "{{ size_total_gib | autoexpand_size_gib }}"

```


## Return Values

  _value (, float, )
    Autoexpand size in GiB\.



## Status

- This  is not guaranteed to have a backwards compatible interface. *[preview]*

- This  is maintained by community.

## Authors

- Job Céspedes Ortiz \(\@jobcespedes\)

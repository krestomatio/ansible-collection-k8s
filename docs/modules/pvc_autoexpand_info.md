# pvc_autoexpand_info
Get autoexpand info

## Synopsis

Get autoexpand info of a mount/pvc\.




## Parameters

  path (True, str, None)
    Path to the mount point \(e\.g\. <code>/mnt/files</code>\)

  increment_gib (optional, int, 5)
    GiB increments when expansion criteria is met

  cap_gib (optional, int, 30)
    Cap / max size in GiB to increase



## Examples

```yaml
    
    - name: Get autoexpand info of mount/pvc
      krestomatio.k8s.pvc_autoexpand_info:
        path: /mypvc
        increment_gib: 5
        cap_gib: 30
      register: pvc_autoexpand_info

```


## Return Values

  status (only when release exists, complex, )
    A dictionary of mount/pvc expand status output\. Fields are camelCase

    sizeAvailableGib (success, float, 0.5)
      Current available storage \(GiB\)

    sizeTotalGib (success, float, 5.0)
      Current total storage\(GiB\)

    expansionRequired (always, bool, False)
      Whether expansion is required if storage available is below percentage

    autoexpandSizeGib (success, int, 10)
      Autoexpansion size after checking available\, total storage\, and defined cap / max size

    capReached (success, bool, False)
      Whether defined cap / max size has been reached




## Status

- This module is not guaranteed to have a backwards compatible interface. *[preview]*

- This module is maintained by community.

## Authors

- Job Céspedes Ortiz \(\@jobcespedes\)

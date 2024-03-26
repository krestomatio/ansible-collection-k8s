# mount_info
Get mount info

## Synopsis

Get mount info\.




## Parameters

  path (True, str, None)
    Path to the mount point \(e\.g\. <code>/mnt/files</code>\)



## Examples

```yaml
    
    - name: Get mount info
      krestomatio.k8s.mount_info:
        path: /mymount
      register: mount_info

```


## Return Values

  mount_info (only when release exists, complex, )
    A dictionary containing information about your mount\.

    block_available (success, int, 32796014)
      Block available

    block_size (success, int, 4096)
      Block size

    block_total (success, int, 57072443)
      Block total

    block_used (success, int, 24276429)
      Block used

    device (success, string, /dev/vda1)
      Device path

    fstype (success, string, ext4)
      FSType

    inode_available (success, int, 128131677)
      INode available

    inode_total (success, int, 131072000)
      INode total

    inode_used (success, int, 2940323)
      INode used

    mount (success, string, /nfs-sample-nfs-pvc)
      Mount path

    options (success, string, rw,relatime,bind)
      Mount options

    size_available (success, int, 134332473344)
      Available size

    size_total (success, int, 233768726528)
      Total size




## Status


## Authors

- Job Céspedes Ortiz \(\@jobcespedes\)

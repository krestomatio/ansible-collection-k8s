#!/usr/bin/python

# Copyright: (c) 2021, Job Céspedes Ortiz <jobcespedes@krestomatio.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: mount_info

short_description: Get mount info

version_added: "2.9.0"

description: Get mount info.

options:
  path:
    description:
      - Path to the mount point (e.g. C(/mnt/files))
    required: true
    type: str

author:
  - "Job Céspedes Ortiz (@jobcespedes)"
'''

EXAMPLES = r'''
- name: Get mount info
  krestomatio.k8s.mount_info:
    path: /mymount
  register: mount_info
'''

RETURN = r'''
mount_info:
  type: complex
  description: A dictionary containing information about your mount.
  returned: only when release exists
  contains:
    block_available:
      description: Block available
      type: int
      returned: success
      sample: 32796014
    block_size:
      description: Block size
      type: int
      returned: success
      sample: 4096
    block_total:
      description: Block total
      type: int
      returned: success
      sample: 57072443
    block_used:
      description: Block used
      type: int
      returned: success
      sample: 24276429
    device:
      description: Device path
      type: string
      returned: success
      sample: "/dev/vda1"
    fstype:
      description: FSType
      type: string
      returned: success
      sample: "ext4"
    inode_available:
      description: INode available
      type: int
      returned: success
      sample: 128131677
    inode_total:
      description: INode total
      type: int
      returned: success
      sample: 131072000
    inode_used:
      description: INode used
      type: int
      returned: success
      sample: 2940323
    mount:
      description: Mount path
      type: string
      returned: success
      sample: "/nfs-sample-nfs-pvc"
    options:
      description: Mount options
      type: string
      returned: success
      sample: "rw,relatime,bind"
    size_available:
      description: Available size
      type: int
      returned: success
      sample: 134332473344
    size_total:
      description: Total size
      type: int
      returned: success
      sample: 233768726528
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible_collections.krestomatio.k8s.plugins.module_utils.storage import get_mount_info


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        mount_info={},
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    # if module.check_mode:
    #     module.exit_json(**result)

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    mount_info = {}
    try:
        mount_info = get_mount_info(module)
    except Exception as e:
        module.fail_json(msg=to_native(e), **result)

    if not mount_info:
        module.fail_json(msg="Mount path is not present", **result)

    result['mount_info'] = mount_info
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

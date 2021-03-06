#!/usr/bin/python

# Copyright: (c) 2021, Job Céspedes Ortiz <jobcespedes@krestomatio.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: pvc_autoexpand_info

short_description: Get autoexpand info

version_added: "2.9.0"

description: Get autoexpand info of a mount/pvc.

options:
  path:
    description:
      - Path to the mount point (e.g. C(/mnt/files))
    required: true
    type: str
  increment_gib:
    description:
      - GiB increments when expansion criteria is met
    default: 5
    type: int
  cap_gib:
    description:
      - Cap / max size in GiB to increase
    default: 30
    type: int

author:
  - "Job Céspedes Ortiz (@jobcespedes)"
'''

EXAMPLES = r'''
- name: Get autoexpand info of mount/pvc
  krestomatio.k8s.pvc_autoexpand_info:
    path: /mypvc
    increment_gib: 5
    cap_gib: 30
  register: pvc_autoexpand_info
'''

RETURN = r'''
status:
  type: complex
  description: A dictionary of mount/pvc expand status output. Fields are camelCase
  returned: only when release exists
  contains:
    sizeAvailableGib:
        description: Current available storage (GiB)
        type: float
        returned: success
        sample: 0.5
    sizeTotalGib:
        description: Current total storage(GiB)
        type: float
        returned: success
        sample: 5.0
    expansionRequired:
        description: Whether expansion is required if storage available is below percentage
        type: bool
        returned: always
        sample: false
    autoexpandSizeGib:
        description: Autoexpansion size after checking available, total storage, and defined cap / max size
        type: int
        returned: success
        sample: 10
    capReached:
        description: Whether defined cap / max size has been reached
        type: bool
        returned: success
        sample: false
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.text.converters import to_native
from ansible_collections.krestomatio.k8s.plugins.module_utils.storage import (
    get_mount_info,
    b_to_gib,
    below_twenty_pct,
    autoexpand_size_gib
)


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        increment_gib=dict(type='int', default=5),
        cap_gib=dict(type='int', default=30)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    expansion_required = False
    status = dict(
        expansionRequired=expansion_required
    )
    result = dict(
        changed=False,
        status=status
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

    increment_gib = module.params['increment_gib']
    cap_gib = module.params['cap_gib']
    size_available = mount_info['size_available']
    size_total = mount_info['size_total']

    size_available_gib = b_to_gib(size_available)
    size_total_gib = b_to_gib(size_total)

    # expansion required threshold: storage available should be below 20%
    # of total storage AND less GiB than 'increment_gib'; otherwise expansion
    # is not required
    if below_twenty_pct(size_available, size_total) and size_available_gib < increment_gib:
        expansion_required = True

    status['sizeAvailableGib'] = b_to_gib(size_available)
    status['sizeTotalGib'] = b_to_gib(size_total)
    status['expansionRequired'] = expansion_required

    this_autoexpand_size_gib = autoexpand_size_gib(
        size_total_gib,
        increment_gib,
        cap_gib,
        expansion_required
    )
    status['autoexpandSizeGib'] = this_autoexpand_size_gib
    status['capReached'] = bool(this_autoexpand_size_gib >= cap_gib)
    result['status'] = status

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

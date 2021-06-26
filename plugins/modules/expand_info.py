#!/usr/bin/python

# Copyright: (c) 2021, Job Céspedes Ortiz <jobcespedes@krestomatio.com>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: expand_info

short_description: Get expand info

version_added: "2.9.0"

description: Get expand info of a mount/pvc.

options:
  path:
    description:
      - Path to the mount point (e.g. C(/mnt/files))
    required: true
    type: str
  increment_gib:
    description:
      - Recommended GiB increments if expansion required
    default: 5
    type: int
  cap_gib:
    description:
      - Cap / max size in GiB to recommend/increment
    default: 250
    type: int

author:
  - "Job Céspedes Ortiz (@jobcespedes)"
'''

EXAMPLES = r'''
- name: Get expand info of mount/pvc
  krestomatio.k8s.expand_info:
    path: /mypvc
    increment_gib: 25
    cap_gib: 250
  register: expand_info
'''

RETURN = r'''
size_available_pct:
    description: Current available storage percentage (%)
    type: float
    returned: success
    sample: 0.1
size_available_gib:
    description: Current available storage (GiB)
    type: float
    returned: success
    sample: 0.5
size_total_gib:
    description: Current total storage(GiB)
    type: float
    returned: success
    sample: 5.0
expansion_required:
    description: Whether expansion is required if storage available is below percentage
    type: bool
    returned: always
    sample: false
recommended_size_gib:
    description: Recommended size after checking available and total storage
    type: int
    returned: success
    sample: 10
cap_reached:
    description: Whether cap / max expansion has been reached
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
    recommended_size_gib
)


def run_module():
    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        path=dict(type='str', required=True),
        increment_gib=dict(type='int', default=5),
        cap_gib=dict(type='int', default=250)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    expansion_required = False
    result = dict(
        changed=False,
        expansion_required=expansion_required
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

    this_recommended_size_gib = recommended_size_gib(size_total_gib, increment_gib, cap_gib, expansion_required)

    result['size_available_gib'] = b_to_gib(size_available)
    result['size_total_gib'] = b_to_gib(size_total)
    result['expansion_required'] = expansion_required
    result['recommended_size_gib'] = this_recommended_size_gib
    result['cap_reached'] = bool(this_recommended_size_gib >= cap_gib)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()

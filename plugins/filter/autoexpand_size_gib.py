from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.krestomatio.k8s.plugins.module_utils.storage import (
    autoexpand_size_gib,
    b_to_gib,
)

DOCUMENTATION = r"""
  name: autoexpand_size_gib
  author: Job Céspedes Ortiz (@jobcespedes)
  short_description: Autoexpand size in GiB
  description: Get autoexpand size in GiB
  positional: _input
  options:
    _input:
      description: Size total GiB
      type: float
      required: true
"""

EXAMPLES = r"""
  autoexpand_size_gib: "{{ size_total_gib | autoexpand_size_gib }}"
"""

RETURN = r"""
  _value:
    description: Autoexpand size in GiB.
    type: float
"""


class FilterModule(object):

    def filters(self):
        return {"autoexpand_size_gib": autoexpand_size_gib}

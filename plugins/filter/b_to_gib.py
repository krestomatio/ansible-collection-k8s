from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.krestomatio.k8s.plugins.module_utils.storage import (
    b_to_gib,
)

DOCUMENTATION = r"""
  name: b_to_gib
  author: Job Céspedes Ortiz (@jobcespedes)
  short_description: Bytes to GiB
  description: Convert bytes to GiB
  positional: _input
  options:
    _input:
      description: Bytes
      type: int
      required: true
"""

EXAMPLES = r"""
  total_gib: "{{ 1024000 | b_to_gib }}"
"""

RETURN = r"""
  _value:
    description: GiB.
    type: float
"""


class FilterModule(object):

    def filters(self):
        return {"b_to_gib": b_to_gib}

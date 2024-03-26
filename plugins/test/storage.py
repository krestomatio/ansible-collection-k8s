from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.krestomatio.k8s.plugins.module_utils.storage import (
    below_twenty_pct,
)


DOCUMENTATION = r"""
  name: below_twenty_pct
  author: Job Céspedes Ortiz (@jobcespedes)
  short_description: Below 20%
  description: Whether size is below 20%
  positional: _input
  options:
    _input:
      description: Size available
      type: float
      required: true
"""

EXAMPLES = r"""
  is_below_twenty_pct: "{{ 80000 | below_twenty_pct }}"
"""

RETURN = r"""
  _value:
    description: Whether size is below 20%.
    type: bool
"""


class TestModule:

    def tests(self):
        return {"below_twenty_pct": below_twenty_pct}

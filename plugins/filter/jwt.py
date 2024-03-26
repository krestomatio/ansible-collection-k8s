from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.krestomatio.k8s.plugins.module_utils.jwt import jwt_token

DOCUMENTATION = r"""
  name: jwt_token
  author: Job Céspedes Ortiz (@jobcespedes)
  short_description: JWT token
  description: Generate a JWT token with a payload
  positional: _input
  options:
    _input:
      description: JWT Payload
      type: string
      required: true
"""

EXAMPLES = r"""
  auth_token: "{{ 'my_payload' | jwt_token }}"
"""

RETURN = r"""
  _value:
    description: JWT Token
    type: string
"""


class FilterModule(object):

    def filters(self):
        return {"jwt_token": jwt_token}

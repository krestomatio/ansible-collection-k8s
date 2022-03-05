from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible_collections.krestomatio.k8s.plugins.module_utils.jwt import jwt_token


class FilterModule(object):

    def filters(self):
        return {
            'jwt_token': jwt_token
        }

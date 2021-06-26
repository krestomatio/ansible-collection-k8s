from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible_collections.krestomatio.k8s.plugins.module_utils.storage import recommended_size_gib, b_to_gib


class FilterModule(object):

    def filters(self):
        return {
            'recommended_size_gib': recommended_size_gib,
            'b_to_gib': b_to_gib
        }

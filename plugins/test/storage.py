from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.krestomatio.k8s.plugins.module_utils.storage import (
    below_twenty_pct,
)




class TestModule:

    def tests(self):
        return {"below_twenty_pct": below_twenty_pct}

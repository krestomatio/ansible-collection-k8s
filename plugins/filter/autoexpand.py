import math


class FilterModule(object):

    def filters(self):
        return {'autoexpand_gib': self.autoexpand_gib}

    def autoexpand_gib(self, current_gib, increment_gib=25,cap_gib=1000):
        autoexpand_gib = int(math.ceil(int(current_gib) / int(increment_gib))) \
            * int(increment_gib) + int(increment_gib)

        if autoexpand_gib < int(cap_gib):
            return autoexpand_gib
        else:
            return int(cap_gib)

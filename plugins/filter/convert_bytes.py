class FilterModule(object):
    def filters(self):
        return {
            'b_to_gib': self.b_to_gib,
        }

    def b_to_gib(self, bytes):
        gib = round(bytes / (1024**3),1)
        return gib

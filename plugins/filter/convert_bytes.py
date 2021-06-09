class FilterModule(object):
    def filters(self):
        return {
            'b_to_gb': self.b_to_gb,
        }

    def b_to_gb(self, bytes):
        gb = round(bytes / (1024**3),1)
        return gb

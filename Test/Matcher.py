class Matcher(object):
    def __init__(self, some_obj):
        self.some_obj = some_obj

    def __eq__(self, other):
        return self.some_obj.compare(other)
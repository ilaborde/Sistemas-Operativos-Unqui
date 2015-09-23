class Instruction:
    cpu = 1
    io = 2

    def __init__(self, text, resourcetype):
        self.text = text
        self.resource = resourcetype


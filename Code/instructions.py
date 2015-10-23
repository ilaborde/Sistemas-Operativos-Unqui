class Instruction:
    cpu = 1
    io = 2
    kill = 3

    Monitor = 4

    def __init__(self, text, type, resourceType):
        self.text = text
        self.type = type
        self.resourceType = resourceType


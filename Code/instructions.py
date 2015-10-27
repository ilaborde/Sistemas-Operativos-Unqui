class InstructionType:
    cpu = 1
    io = 2
    kill = 3


class ResourceType:
    Monitor = 1


class Instruction:
    def __init__(self, text, type, resourcetype):
        self.text = text
        self.type = type
        self.resourceType = resourcetype

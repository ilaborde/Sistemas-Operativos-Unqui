class InstructionType:
    cpu = 1
    io = 2
    kill = 3


class ResourceType:
    Monitor = 1


class Instruction:
    def __init__(self, text, type, resourcetype):
        self.text = text
        self.type = type ##type of instruction
        self.resourceType = resourcetype ##type of resource(e: monitor)

class memoryFrame:

    def __init__(self,id, markSize):
        self.instructions = {}
        self.markSize = markSize
        self.id = 0

    def getData(self):
        return self.data

    def putInstruction(self, instruction):
        if len(self.instructions) < self.markSize:
            self.instructions.append(instruction)
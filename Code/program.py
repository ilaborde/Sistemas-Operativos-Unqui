class Program:
    def __init__(self):
        self.instructions = []

    def add(self, instruction):
        self.instructions.append(instruction)

    def run(self):
        for x in self.instructions:
            x.imprimir()

    def instructionsSize(self):
        return len(self.instructions)

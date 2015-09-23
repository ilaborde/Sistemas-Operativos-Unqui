class Memory:
    def __init__(self):
        self.cells = []

    def put(self, programInstructions):
        # add instructions to the list and returns the program index

        self.cells = self.cells + programInstructions
        return len(self.cells) - len(programInstructions)

    def get(self, index):
        return self.cells[index]

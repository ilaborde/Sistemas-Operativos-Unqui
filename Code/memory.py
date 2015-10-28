class Memory:
    def __init__(self):
        self.cells = []

    def put(self, programinstructions):
        # add instructions to the list and returns the program index
        self.cells = self.cells + programinstructions
        return len(self.cells) - len(programinstructions)

    def get(self, index):
        return self.cells[index]

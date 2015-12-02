class Memory:
    def __init__(self, lockInstructions):
        self.cells = []
        self.lockInstructions= lockInstructions
    def put(self, programinstructions):
        # add instructions to the list and returns the program index
        self.lockInstructions.acquire()
        self.cells = self.cells + programinstructions
        self.lockInstructions.release()
        return len(self.cells) - len(programinstructions)

    def get(self, index):
        #Obtain a instruction contained in the cell of the memory
        cell= self.cells[index]
        return cell











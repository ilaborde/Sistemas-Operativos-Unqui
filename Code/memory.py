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

        self.lockInstructions.acquire()
        cell= self.cells[index]
        self.lockInstructions.release()
        return cell

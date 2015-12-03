from Code.memoryFrame import MemoryFrame


class Memory:
    def __init__(self, lockInstructions):
        self.cells = [None]*16
        self.lockInstructions= lockInstructions

    def put(self, index, instruction):
        # add instructions to the list and returns the program index
        self.lockInstructions.acquire()
        self.cells[index] = instruction
        self.lockInstructions.release()

    def get(self, index):
        #Obtain a instruction contained in the cell of the memory
        cell= self.cells[index]
        return cell











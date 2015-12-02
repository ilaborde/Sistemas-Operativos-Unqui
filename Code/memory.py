from Code.memoryBlock import memoryBlock


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


class MemoryPaging:

    def __init__(self, lockInstructions):
        self.cells = []
        self.lockInstructions = lockInstructions

    def initializeMemory(self, memoryCapacity):

        for physicalMemoryDirection in range(memoryCapacity):
            self.cells[physicalMemoryDirection] = memoryBlock()

    def putData(self, instruction, index):
        # add instructions to the list and returns the program index
        self.lockInstructions.acquire()
        self.cells[index].putData(instruction)
        self.lockInstructions.release()

    def get(self, index):
        #get a instruction contained in the cell of the memory
        self.lockInstructions.acquire()
        cell= self.cells[index]
        self.lockInstructions.release()
        return cell.getData()









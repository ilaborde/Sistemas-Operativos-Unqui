class MemoryManager:

    def __init__(self, memory):
        self.pageTableDictionary= {}
        self.memory= memory

    def registryPageTableForPcb(self, pcb, pageTable):
        self.pageTableDictionary[pcb] = pageTable

    def createPageTableForPcb(self, pcb):
        newPageTable= []
        self.registryPageTableForPcb(pcb, newPageTable)

    def addFramesToPageTable(self, instruction, pcb):
        pageTableToAdd= self.pageTableDictionary[pcb]
        blockToAddData= self.getBlockMemoryEmpty()

        if not blockToAddData == None:
          pageTableToAdd[len(pageTableToAdd)] = "1" #TODO Calculate markNumber
          blockToAddData.putData(instruction)
          self.registryPageTableForPcb(pcb, pageTableToAdd)

    def getBlockMemoryEmpty(self):
        count= 0
        while count < len(self.memory.cells):
            if self.memory.cells[count].isEmpty:
               return self.memory.cells[count]
        return None
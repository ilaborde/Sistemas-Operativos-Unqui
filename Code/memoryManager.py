class MemoryManager:

    def __init__(self, memory):
        self.pageTableDictionary= {}
        self.memory= memory

    def registryPageTableForPcb(self, pcb, pageTable):
        self.pageTableDictionary[pcb] = pageTable

    def createPageTableForPcb(self, program, pcb):
      newPageTable= []
      pageIndex= 0
      count= 0

      while len(program.instructions) > count:
          newPageTable[pageIndex] = "1"
          pageIndex += 1
          count += 1

      self.registryPageTableForPcb(pcb, newPageTable)

    def getBlockMemoryEmpty(self):
        count= 0
        while count < len(self.memory.cells):
            if self.memory.cells[count].isEmpty:
               return self.memory.cells[count]
        return None
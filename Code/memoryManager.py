from queue import Queue
from Code.memoryFrame import MemoryFrame


class MemoryManager:
    def __init__(self, memory):
        self.pageTableList = {}
        self.memory = memory
        ##create memory frames free
        ##todo move to factory
        self.freeMemoryFrames = Queue()
        for i in range(0, int((len(memory.cells) / 4))):
            self.freeMemoryFrames.put(MemoryFrame(i + 1, 4, i))

    # def registryPageTableForPcb(self, pcb, pageTable):
    #     self.pageTableList[pcb.pid] = pageTable
    #
    # def createPageTableForPcb(self, pcb):
    #     newPageTable= []
    #     self.registryPageTableForPcb(pcb, newPageTable)
    #
    # def addPagesToPageTable(self, pcb):
    #     pageTableToAdd= self.pageTableList[pcb.pid]
    #
    #     pageCount= pcb.programLength / 4
    #     pageIndex = 0
    #
    #     while not pageCount == 0:
    #         pageTableToAdd[pageIndex] = None
    #         pageIndex += 1
    #         pageCount -= 1
    #
    #     self.registryPageTableForPcb(pcb, pageTableToAdd)


    def loadToMemory(self, pcb, instructions):
        # calculate page count
        pageCount = pcb.programLength / 4
        # get a free Frame
        frame = self.freeMemoryFrames.get()
        curretPageTable = {}
        pageIndex = 0
        while not pageCount == 0:
            curretPageTable[pageIndex] = None
            pageIndex += 1
            pageCount -= 1

        curretPageTable[0] = frame
        self.writeToMemory(frame.addressBase, instructions)
        self.pageTableList[pcb.pid] = curretPageTable

    def writeToMemory(self, addressBase, instructions):
        for i in range(addressBase, addressBase + 4):
            self.memory.put(i, instructions[i])

    def getInstrucction(self, pcb):
        frame = self.pageTableList.get(pcb.pid)
        frame[pcb.pc + self.currentPcb.memoryPosition]
        # devuelve la instruccion que sigue, si no esta, va a buscarla a disco y la carga al page table
        # busca la tabla del pcb
        # calcula donde la instruccion y la devuelve
        pass

    def release(self, pcb):
        # busca la tabla del pcb
        # borra la tabla de pagina
        # pone el marco en la lista de marcos libres
        pass

from queue import Queue
from Code.memoryFrame import memoryFrame


class MemoryManager:

    def __init__(self, memory):
        self.pageTableList= {}
        ##create memory frames free
        ##todo move to factory
        self.freeMemoryFrames = Queue()
        for i in  range(0,10):
            self.freeMemoryFrames.put(memoryFrame(i,4))

        self.memory= memory

    def registryPageTableForPcb(self, pcb, pageTable):
        self.pageTableList[pcb.pid] = pageTable

    def createPageTableForPcb(self, pcb):
        newPageTable= []
        self.registryPageTableForPcb(pcb, newPageTable)

    def addPagesToPageTable(self, pcb):
        pageTableToAdd= self.pageTableList[pcb.pid]

        pageCount= pcb.programLength / 4
        pageIndex = 0

        while not pageCount == 0:
            pageTableToAdd[pageIndex] = None
            pageIndex += 1
            pageCount -= 1

        self.registryPageTableForPcb(pcb, pageTableToAdd)

    def loadToMemory(self,pcb):

        pageTable = self.pageTableList.get(pcb.id,None)
        if pageTable is None:
           #get count of instrucctions
            pageCount= pcb.programLength / 4
            frame = self.freeMemoryFrames.get()
            curretPageTable ={}
            pageIndex = 0
            while not pageCount == 0:
                curretPageTable[pageIndex] = None
                pageIndex += 1
                pageCount -= 1

            curretPageTable[0] = frame
            self.pageTableList[pcb.id] = curretPageTable
        else:

            emptyFrame = self.freeMemoryFrames.get()
            emptyFrame.putInstruction()
            pageTable[1] = emptyFrame


    def getInstrucction(self,pcb):
        frame = self.pageTableList.get(pcb.id)
        frame[pcb.pc + self.currentPcb.memoryPosition]
        #devuelve la instruccion que sigue, si no esta, va a buscarla a disco y la carga al page table
        #busca la tabla del pcb
        #calcula donde la instruccion y la devuelve
        pass

    def release(self,pcb):
        #busca la tabla del pcb
        #borra la tabla de pagina
        #pone el marco en la lista de marcos libres
        pass
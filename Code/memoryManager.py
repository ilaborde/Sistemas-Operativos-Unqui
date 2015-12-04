from queue import Queue
from Code.memoryFrame import MemoryFrame


class MemoryManager:
    def __init__(self, memory,disk):
        self.pageTableList = {}
        self.memory = memory
        self.disk = disk
        ##create memory frames free
        ##todo move to factory
        self.freeMemoryFrames = Queue()
        for i in range(0, int((len(memory.cells) / 4))):
            self.freeMemoryFrames.put(MemoryFrame(i + 1, 4, i*4))

    def loadToMemory(self, pcb, instructions):
        # calculate page count
        if pcb.programLength // 4  == 0:
            pageCount = pcb.programLength / 4
        else:
            pageCount = pcb.programLength // 4 + 1

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
        # to = addressBase + 4
        # if(len(instructions) < to):
        #     to = len(instructions)
        for i in range(addressBase, addressBase + 4):
            if instructions.qsize() > 0:
                self.memory.put(i, instructions.get())

    def getInstrucction(self, pcb):
        tables = self.pageTableList.get(pcb.pid)
        pageNumber = (pcb.pc // 4)
        frame = tables.get(pageNumber,None) #get page
        if frame is not None:
            modInstruction = pcb.pc % 4# get instruction
            instruction = self.memory.get(frame.addressBase,modInstruction )
        else:
            frame = self.freeMemoryFrames.get()
            tables[pageNumber] = frame
            program = self.disk.getProgram(pcb.programName)
            self.writeToMemory(frame.addressBase, program.instructions)
            modInstruction = pcb.pc % 4# get instruction
            instruction = self.memory.get(frame.addressBase,modInstruction )

        return instruction

    def release(self, pcb):
        frames = self.pageTableList.get(pcb.pid)
        for e in range(0, len(frames)):
            self.freeMemoryFrames.put(frames[e])
        self.pageTableList.pop(pcb.pid)
        # borra la tabla de pagina
        # pone el marco en la lista de marcos libres

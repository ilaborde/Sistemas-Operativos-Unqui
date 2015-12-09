from queue import Queue
from Code.memoryFrame import MemoryFrame
from Code.page import Page


class MemoryManager:

    def __init__(self, memory,disk, swapDisk):
        self.pageTableList = {}
        self.memory = memory
        self.disk = disk
        ##create memory frames free
        ##todo move to factory
        self.freeMemoryFrames = Queue()
        self.lastInstructionPositionForPcb = {}
        for i in range(0, int((len(memory.cells) / 4))):
            self.freeMemoryFrames.put(MemoryFrame(i + 1, 4, i*4))

        self.lastRecentlyUsedPage= None
        self.currentIdPage= 0
        self.swapDisk= swapDisk

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
            curretPageTable[pageIndex] = Page(self.currentIdPage, pcb.pid)
            pageIndex += 1
            pageCount -= 1
            self.currentIdPage += 1

        page= curretPageTable[0]
        page.registryFrame(frame)
        self.writeToMemory(frame.addressBase, instructions, pcb, False)
        self.pageTableList[pcb.pid] = curretPageTable

    def writeToMemory(self, addressBase, instructions, pcb, loadFromSwap):

        max= addressBase + 4
        index= addressBase
        count= self.lastInstructionPositionForPcb.get(pcb.pid, None)

        if count == None or loadFromSwap:
            count = 0


        while (not index == max):
             try:
                self.memory.put(index, instructions[count])
             except:
                 pass
             index += 1
             count += 1
        self.lastInstructionPositionForPcb[pcb.pid] = count
        # for i in range(addressBase, addressBase + 4):
        #     if len(instructions)> 0:
        #         self.memory.put(i, instructions[pcb.pc])

    def getInstrucction(self, pcb):
        tableOfPcb = self.pageTableList.get(pcb.pid)
        pageNumber = (pcb.pc // 4)
        page = tableOfPcb.get(pageNumber,None) #get page


        if page == None:
           page=  self.swapDisk.getPage(pcb.pid)
           tableOfPcb[pageNumber] = page
           self.cleanInstructionsOnMemory(page.frame)
           program = self.disk.getProgram(pcb.programName)
           self.writeToMemory(page.frame.addressBase, self.swapDisk.getInstructionsInSwap(pcb.pid), pcb, True)
           modInstruction = pcb.pc % 4# get instruction
           instruction = self.memory.get(page.frame.addressBase,modInstruction )
        else:
            if page.frame is not None:
                modInstruction = pcb.pc % 4# get instruction
                instruction = self.memory.get(page.frame.addressBase,modInstruction )
            else:
                if self.freeMemoryFrames.qsize() > 0:
                    frame = self.freeMemoryFrames.get()
                    page= tableOfPcb[pageNumber]
                    page.registryFrame(frame)
                    program = self.disk.getProgram(pcb.programName)
                    self.writeToMemory(frame.addressBase, program.instructions, pcb, False)
                    modInstruction = pcb.pc % 4# get instruction
                    instruction = self.memory.get(frame.addressBase,modInstruction )
                else:
                    self.releasePageAndPutOnSwapDisk(self.lastRecentlyUsedPage, pcb)
                    frame = self.freeMemoryFrames.get()
                    page= tableOfPcb[pageNumber]
                    page.registryFrame(frame)
                    program = self.disk.getProgram(pcb.programName)
                    self.writeToMemory(frame.addressBase, program.instructions, pcb, False)
                    modInstruction = pcb.pc % 4# get instruction
                    instruction = self.memory.get(frame.addressBase,modInstruction )


        if self.lastRecentlyUsedPage== None:
            self.lastRecentlyUsedPage= page

        if not self.lastRecentlyUsedPage == None:
            if page.frecuencyCount < self.lastRecentlyUsedPage.frecuencyCount:
                self.lastRecentlyUsedPage= page

        page.incrementFrecuencyCount()
        return instruction

    def release(self, pcb):
        pages = self.pageTableList.get(pcb.pid)
        for e in range(0, len(pages)):
            self.freeMemoryFrames.put(pages[e].frame)
        self.pageTableList.pop(pcb.pid)

    def releasePageAndPutOnSwapDisk(self, LastRecentlyUsedPage, pcb):
        #todo hacer swap, recuperar instrucciones
        pageDeleted= self.deletePage(LastRecentlyUsedPage)
        frame= pageDeleted.frame
        frame.isInSwapping = True

        self.freeMemoryFrames.put(frame)
        instructionsDeleted= self.cleanInstructionsOnMemory(frame)

        self.swapDisk.writePageAndInstructionsInSwap(pageDeleted, pageDeleted.pid, instructionsDeleted)

    def deletePage(self, pageToDelete):

        count1= 1

        while not count1 > len(self.pageTableList):
            try:
                count2= 0
                page= self.pageTableList[count1]
                while not count2 > len(page):
                    try:
                        if (page[count2].id == pageToDelete.id):
                             pageDeleted= page[count2]
                             page.pop(count2)
                    except:
                        pass
                    count2 +=1
            except:
                pass
            count1 +=1

        return pageDeleted


    def cleanInstructionsOnMemory(self, frame):

        instructionsDeleted= []
        for i in range(frame.addressBase, frame.addressBase + 4 ):
            try:
                instructionsDeleted.append(self.memory.cells[i])
                self.memory.cells[i] = None
            except:
                pass

        return instructionsDeleted

    def writeInstructionsOnMemory(self, frame, instructions):

        count= 0
        for i in range(frame.addressBase, frame.addressBase + 4 ):
            try:
                self.memory.cells[i] = instructions[count]
                count += 1
            except:
                pass


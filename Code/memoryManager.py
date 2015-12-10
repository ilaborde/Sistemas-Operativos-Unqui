from queue import Queue
from Code.memoryFrame import MemoryFrame
from Code.page import Page


class MemoryManager:
    def __init__(self, memory, disk, swapDisk, frames):
        self.pageTableList = {}
        self.memory = memory
        self.disk = disk
        self.freeMemoryFrames = frames
        self.lastInstructionPositionForPcb = {}
        self.lastRecentlyUsedPage = None
        self.currentIdPage = 0
        self.swapDisk = swapDisk

    def loadToMemory(self, pcb, instructions):
        # calculate page count
        if pcb.programLength // 4 == 0:
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

        page = curretPageTable[0]
        page.registryFrame(frame)
        self.writeToMemory(frame.addressBase, instructions, pcb, False)
        self.pageTableList[pcb.pid] = curretPageTable

    def writeToMemory(self, addressBase, instructions, pcb, loadFromSwap):

        max = addressBase + 4
        index = addressBase
        count = self.lastInstructionPositionForPcb.get(pcb.pid, None)

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

    def getInstrucction(self, pcb):
        tableOfPcb = self.pageTableList.get(pcb.pid)
        pageNumber = (pcb.pc // 4)
        page = tableOfPcb.get(pageNumber, None)  # get page
        modInstruction = pcb.pc % 4  # get instruction
        program = self.disk.getProgram(pcb.programName)

        if page == None:
            page = self.swapDisk.getPage(pcb.pid)
            tableOfPcb[pageNumber] = page
            self.cleanInstructionsOnMemory(page.frame)
            self.writeToMemory(page.frame.addressBase, self.swapDisk.getInstructionsInSwap(pcb.pid), pcb, True)
            instruction = self.memory.get(page.frame.addressBase, modInstruction)
        else:
            if page.frame is not None:
                instruction = self.memory.get(page.frame.addressBase, modInstruction)
            else:
                if self.freeMemoryFrames.qsize() > 0:
                    frame = self.freeMemoryFrames.get()
                    page = tableOfPcb[pageNumber]
                    page.registryFrame(frame)
                    self.writeToMemory(frame.addressBase, program.instructions, pcb, False)
                    instruction = self.memory.get(frame.addressBase, modInstruction)
                else:
                    self.releasePageAndPutOnSwapDisk(self.getLastRecentlyUsedPage(), pcb)
                    frame = self.freeMemoryFrames.get()
                    page = tableOfPcb[pageNumber]
                    page.registryFrame(frame)
                    self.writeToMemory(frame.addressBase, program.instructions, pcb, False)
                    instruction = self.memory.get(frame.addressBase, modInstruction)

        page.incrementFrecuencyCount()
        return instruction

    def release(self, pcb):
        pages = self.pageTableList.get(pcb.pid)
        for e in range(0, len(pages)):
            self.freeMemoryFrames.put(pages[e].frame)
        self.pageTableList.pop(pcb.pid)

    def releasePageAndPutOnSwapDisk(self, LastRecentlyUsedPage, pcb):
        # todo do swap, get instructions
        pageDeleted = self.deletePage(LastRecentlyUsedPage)
        frame = pageDeleted.frame
        frame.isInSwapping = True
        self.freeMemoryFrames.put(frame)
        instructionsDeleted = self.cleanInstructionsOnMemory(frame)
        self.swapDisk.writePageAndInstructionsInSwap(pageDeleted, pageDeleted.pid, instructionsDeleted)

    def deletePage(self, pageToDelete):
        count1 = 1
        while not count1 > len(self.pageTableList):
            try:
                count2 = 0
                pageTable = self.pageTableList[count1]
                while not count2 > len(pageTable):
                    try:
                        if (pageTable[count2].id == pageToDelete.id):
                            pageDeleted = pageTable[count2]
                            pageTable.pop(count2)
                    except:
                        pass
                    count2 += 1
            except:
                pass
            count1 += 1

        return pageDeleted

    def cleanInstructionsOnMemory(self, frame):

        instructionsDeleted = []
        for i in range(frame.addressBase, frame.addressBase + 4):
            try:
                instructionsDeleted.append(self.memory.cells[i])
                self.memory.cells[i] = None
            except:
                pass

        return instructionsDeleted

    def getLastRecentlyUsedPage(self):

        count1 = 1
        pageAux = self.pageTableList[count1][0]
        while not count1 > len(self.pageTableList):
            try:
                count2 = 0
                pageTable = self.pageTableList[count1]
                while not count2 > len(pageTable):
                    try:
                        if \
                                        pageTable[count2].frecuencyCount < pageAux.frecuencyCount and not pageTable[count2].frame is None:
                            pageAux = pageTable[count2]
                    except:
                        pass
                    count2 += 1
            except:
                pass
            count1 += 1

        return pageAux

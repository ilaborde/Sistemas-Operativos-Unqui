class SwapDisk:

    def __init__(self):
        self.pageListInSwap= {}
        self.instructions= {}

    def writePageAndInstructionsInSwap(self, page, pid, instructions):
        self.pageListInSwap[pid] = page
        self.instructions[pid] = instructions

    def getPage(self, pid):
        page= self.pageListInSwap[pid]
        self.pageListInSwap.pop(pid)
        return page

    def getInstructionsInSwap(self, pid):
        instructions= self.instructions[pid]
        self.instructions.pop(pid)
        return instructions
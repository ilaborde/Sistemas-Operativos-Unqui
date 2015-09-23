class Pcb:

    def __init__(self, position, count):
        self.pc = 0
        self.PcbId = 1
        self.memoryPosition = position
        self.programCount = count
    
    def IncrementPc(self):
        self.pc = self.pc + 1


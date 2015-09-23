from Code.IRQ import IRQ
from Code.instructions import Instruction


class Cpu:
    def __init__(self, memo, handle):

        self.memory = memo
        self.interruptionManager = handle

    def setPcb(self, pcb):
        self.currentPcb = pcb

    def fetch(self):
        # obtiene una celda de memoria calculando el program counter
        # del currentPcb mas la celda de memoria actual
        cell = self.memory.get(self.currentPcb.pc + self.currentPcb.memoryPosition)

        if cell.resource == Instruction.cpu:
            print(cell.text)
            self.currentPcb.IncrementPc()
            # end of the program
            if self.currentPcb.pc == self.currentPcb.programCount:
                return self.interruptionManager.handle(IRQ(IRQ.kill, self.currentPcb))
        elif cell.resource == Instruction.io:
            self.interruptionManager.handle(IRQ(IRQ.IO, self.currentPcb))

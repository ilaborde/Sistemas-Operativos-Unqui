from Code.IRQ import IRQ
from Code.instructions import Instruction


class Cpu:
    def __init__(self, memory, handle):
        self.memory = memory
        self.interruptionManager = handle

    def setPcb(self, pcb):
        self.currentPcb = pcb

    def fetch(self):
        if self.currentPcb is not None:
            if self.currentPcb.pc == self.currentPcb.programLength:
                # end of the program
                self.interruptionManager.handle(IRQ(IRQ.kill, self.currentPcb))
                return
            # obtiene una celda de memoria calculando el program counter
            # del currentPcb mas la celda de memoria actual
            cell = self.memory.get(self.currentPcb.pc + self.currentPcb.memoryPosition)
            self.currentPcb.incrementPc()

            if cell.resource == Instruction.cpu:
                print(cell.text)

            elif cell.resource == Instruction.io:
                self.interruptionManager.handle(IRQ(IRQ.IO, self.currentPcb))

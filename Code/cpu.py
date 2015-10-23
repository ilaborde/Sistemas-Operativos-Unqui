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
            # get a cell from memory using program counter + currentpcb.memoryPosition
            cell = self.memory.get(self.currentPcb.pc + self.currentPcb.memoryPosition)
            if cell.type == Instruction.kill:
                # end of the program
                self.interruptionManager.handle(IRQ(IRQ.kill, self.currentPcb))
                return

            self.currentPcb.incrementPc()

            if cell.type == Instruction.cpu:
                print(cell.text)

            elif cell.type == Instruction.io:
                self.interruptionManager.handle(IRQ(IRQ.IO, self.currentPcb))

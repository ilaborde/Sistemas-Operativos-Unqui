from Code.IRQ import IRQ
from Code.instructions import InstructionType
from Code.instructions import Instruction


class Cpu:
    def __init__(self, memory, handle):
        self.memory = memory
        self.interruptionManager = handle
        self.currentPcb = None

    def setPcb(self, pcb):
        self.currentPcb = pcb

    def fetch(self):
        if self.currentPcb is not None:
            # get a cell from memory using program counter + currentpcb.memoryPosition
            cell = self.memory.get(self.currentPcb.pc + self.currentPcb.memoryPosition)
            if cell.type == InstructionType.kill:
                # end of the program
                self.interruptionManager.handle(IRQ(IRQ.kill, self.currentPcb))
                return

            if cell.type == InstructionType.cpu:
                print(cell.text)

            elif cell.type == InstructionType.io:
                self.interruptionManager.handle(IRQ(IRQ.IO, self.currentPcb))

            self.currentPcb.incrementPc()
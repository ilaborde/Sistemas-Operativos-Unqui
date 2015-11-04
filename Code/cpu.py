from Code.IRQ import IRQ
from Code.instructions import InstructionType


class Cpu:
    def __init__(self, memory, interruptionmanager):
        self.memory = memory
        self.interruptionManager = interruptionmanager
        self.currentPcb = None
        self.quantum = 0

    def setPcb(self, pcb, quantum):
        self.currentPcb = pcb
        self.quantum = quantum

    def fetch(self):
        if self.currentPcb is not None:
            while self.quantum > 0:
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
                    return

                self.currentPcb.incrementPc()
                self.quantum -= 1

            self.interruptionManager.handle(IRQ(IRQ.timeOut, self.currentPcb))

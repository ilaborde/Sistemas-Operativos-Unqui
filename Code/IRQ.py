##Interruption request
class IRQ:
    kill = 1
    timeOut = 2
    IO = 3
    EndIO = 4
    New = 5

    def __init__(self, irqtype, pcb,instruction, cpu):
        self.type = irqtype
        self.currentPcb = pcb
        self.instruction = instruction
        self.currentCpu= cpu

    def compare(self, other):
        if not type(self) == type(other):
            return False
        if self.type != other.type:
            return False
        if self.currentPcb != other.currentPcb:
            return False
        return True

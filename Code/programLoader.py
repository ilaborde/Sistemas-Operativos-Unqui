from Code.IRQ import IRQ
from Code.pcb import Pcb


class ProgramLoader:
    def __init__(self,disk,memory,interruptionManager):
        self.disk = disk
        self.interruptionManager = interruptionManager
        self.memory = memory

    def load(self,programName):
        program = self.disk.getProgram(programName)
        pcb = self.createPcb(program)
        irq = IRQ(IRQ.New,pcb)
        self.interruptionManager.handle(irq)

    def createPcb(self,program):
        initialPosition = self.memory.put(program.instructions)
        return Pcb(initialPosition, len(program.instructions))
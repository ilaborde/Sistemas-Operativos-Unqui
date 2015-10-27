from Code.IRQ import IRQ
from Code.pcb import Pcb


class ProgramLoader:
    def __init__(self, disk, memory, interruptionmanager):
        self.disk = disk
        self.interruptionManager = interruptionmanager
        self.memory = memory

    def load(self, programname):
        program = self.disk.getProgram(programname)
        pcb = self.createPcb(program)
        irq = IRQ(IRQ.New, pcb)
        self.interruptionManager.handle(irq)

    def createPcb(self, program):
        initialposition = self.memory.put(program.instructions)
        return Pcb(initialposition, len(program.instructions))

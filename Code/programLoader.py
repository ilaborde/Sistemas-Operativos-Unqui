from Code.IRQ import IRQ
from Code.pcb import Pcb


class ProgramLoader:
    def __init__(self, disk, memory, interruptionmanager, pcbtable, lockIrq):
        self.disk = disk
        self.interruptionManager = interruptionmanager
        self.memory = memory
        self.pcbTable = pcbtable
        self.lockIrq= lockIrq

    def load(self, programname):
        self.lockIrq.acquire()
        program = self.disk.getProgram(programname)
        pcb = self.createPcb(program)
        self.pcbTable.addpcb(pcb)
        irq = IRQ(IRQ.New, pcb)
        self.interruptionManager.handle(irq)
        self.lockIrq.wait()
        self.lockIrq.release()

    def createPcb(self, program):
        initialposition = self.memory.put(program.instructions)
        pid = self.pcbTable.getnewpid()
        return Pcb(initialposition, pid, len(program.instructions))

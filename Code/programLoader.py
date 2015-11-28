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
        #create pcb and trigger the new handle interruption
        program = self.disk.getProgram(programname)
        if program is not None:
            self.lockIrq.acquire()
            pcb = self.createPcb(program)
            self.pcbTable.addpcb(pcb)
            irq = IRQ(IRQ.New, pcb)
            self.interruptionManager.handle(irq)
            self.lockIrq.wait()
            self.lockIrq.release()
        else:
            print ("Program not found")

    def createPcb(self, program):
        #create a pcb and loads the program in memory
        initialposition = self.memory.put(program.instructions)
        pid = self.pcbTable.getnewpid()
        return Pcb(initialposition, pid, len(program.instructions))

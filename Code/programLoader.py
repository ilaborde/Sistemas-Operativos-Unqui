from Code.IRQ import IRQ
from Code.pcb import Pcb


class ProgramLoader:
    def __init__(self, disk, memoryManager, interruptionmanager, pcbtable, lockIrq):
        self.disk = disk
        self.interruptionManager = interruptionmanager
        self.memoryManager = memoryManager
        self.pcbTable = pcbtable
        self.lockIrq= lockIrq

    def load(self, programname):
        #create pcb and trigger the new handle interruption
        program = self.disk.getProgram(programname)
        if program is not None:
            self.lockIrq.acquire()
            pcb = self.createPcb(program,programname)
            self.pcbTable.addpcb(pcb)
            self.memoryManager.loadToMemory(pcb,program.instructions)
            irq = IRQ(IRQ.New, pcb,None, None)
            self.interruptionManager.handle(irq)
            self.lockIrq.wait()
            self.lockIrq.release()
        else:
            print ("Program not found")

    def createPcb(self, program, name):
        #create a pcb and loads the program in memory
        pid = self.pcbTable.getnewpid()
        return Pcb(pid, len(program.instructions), name)

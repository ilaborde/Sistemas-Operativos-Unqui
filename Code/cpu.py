from threading import Thread
from Code.IRQ import IRQ
from Code.instructions import InstructionType


class Cpu:

    def __init__(self, memoryManager, interruptionmanager, lockPcb, irqQueue, lockIrqQueue, lockInstructions):
        self.memoryManager = memoryManager
        self.interruptionManager = interruptionmanager
        self.currentPcb = None
        self.quantum = 0
        self.lockPcb= lockPcb
        self.lockIrqQueue= lockIrqQueue
        self.irqQueue= irqQueue
        self.lockInstructions= lockInstructions

    def setPcb(self, pcb, quantum):
        #Set a quantum and a pcb into cpu to process it

        self.currentPcb = pcb
        self.quantum = quantum

    def fetch(self):
        #Process the pcb when the clock calls this method of the cpu
        if self.currentPcb is not None:
            if self.quantum > 0:
                self.processPcb()
            else:
                self.interruptionManager.handle(IRQ(IRQ.timeOut, self.currentPcb,None))
                return True

    def processPcb(self):
        # get a cell from memory using program counter + currentpcb.memoryPosition
        self.lockInstructions.acquire()
        instruction = self.memoryManager.getInstrucction(self.currentPcb)
        self.lockInstructions.release()
        if instruction.type == InstructionType.kill:
            # end of the program
            print(instruction.text + ', pid: ' + str(self.currentPcb.pid))
            self.interruptionManager.handle(IRQ(IRQ.kill, self.currentPcb,instruction))
            return True

        if instruction.type == InstructionType.cpu:
            print(instruction.text + ', pid: ' + str(self.currentPcb.pid))
            self.currentPcb.incrementPc()
            self.quantum -= 1
            return False

        if instruction.type == InstructionType.io:
            self.interruptionManager.handle(IRQ(IRQ.IO, self.currentPcb,instruction))
            return True








from threading import Thread
from Code.IRQ import IRQ
from Code.instructions import InstructionType


class Cpu:

    def __init__(self, memory, interruptionmanager, lockPcb, irqQueue, lockIrqQueue, lockInstructions):
        self.memory = memory
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
            self.processPcb()

    def processPcb(self):

       if self.quantum > 0:
            # get a cell from memory using program counter + currentpcb.memoryPosition
            self.lockInstructions.acquire()
            cell = self.memory.get(self.currentPcb.pc + self.currentPcb.memoryPosition)
            self.lockInstructions.release()
            if cell.type == InstructionType.kill:
                # end of the program
                print(cell.text + ', pid: ' + str(self.currentPcb.pid))
                self.interruptionManager.handle(IRQ(IRQ.kill, self.currentPcb))
                return

            if cell.type == InstructionType.cpu:
                print(cell.text + ', pid: ' + str(self.currentPcb.pid))

            if cell.type == InstructionType.io:
                self.interruptionManager.handle(IRQ(IRQ.IO, self.currentPcb))
                return True

            self.currentPcb.incrementPc()
            self.quantum -= 1
            return False
       else:
            self.interruptionManager.handle(IRQ(IRQ.timeOut, self.currentPcb))
            return True





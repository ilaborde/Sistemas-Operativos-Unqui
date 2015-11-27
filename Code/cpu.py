from threading import Thread
from Code.IRQ import IRQ
from Code.instructions import InstructionType


class Cpu():

    def __init__(self, memory, interruptionmanager, lockPcb, irqQueue, lockIrqQueue):
        self.memory = memory
        self.interruptionManager = interruptionmanager
        self.currentPcb = None
        self.quantum = 0
        self.lockPcb= lockPcb
        self.lockIrqQueue= lockIrqQueue
        self.irqQueue= irqQueue

    def setPcb(self, pcb, quantum):
        #Set a quantum and a pcb into cpu to process it

        self.currentPcb = pcb
        self.quantum = quantum

    def fetch(self):
        #Process the pcb when the clock calls this method of the cpu
        if self.currentPcb is not None:
            self.processPcb()

    def processPcb(self):

       while self.quantum > 0:
            # get a cell from memory using program counter + currentpcb.memoryPosition
            cell = self.memory.get(self.currentPcb.pc + self.currentPcb.memoryPosition)
            if cell.type == InstructionType.kill:
                # end of the program
                print(cell.text + ', pid: ' + str(self.currentPcb.pid))
                self.lockIrqQueue.acquire()
                self.interruptionManager.handle(IRQ(IRQ.kill, self.currentPcb))
                self.lockIrqQueue.release()
                return

            if cell.type == InstructionType.cpu:
                print(cell.text + ', pid: ' + str(self.currentPcb.pid))

            if cell.type == InstructionType.io:
                self.lockIrqQueue.acquire()
                self.interruptionManager.handle(IRQ(IRQ.IO, self.currentPcb))
                self.lockIrqQueue.release()
                return

            self.currentPcb.incrementPc()
            self.quantum -= 1
       self.lockIrqQueue.acquire()
       self.interruptionManager.handle(IRQ(IRQ.timeOut, self.currentPcb))
       self.lockIrqQueue.release()





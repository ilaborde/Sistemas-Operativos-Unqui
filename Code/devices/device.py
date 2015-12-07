from queue import Queue
from threading import Thread
import time
from Code.IRQ import IRQ


class Device(Thread):

    def __init__(self, interruptionManager, queue, lockInstructions):
       Thread.__init__(self)
       self.interruptionManager= interruptionManager
       self.queue= queue
       self.lockInstructions= lockInstructions

    def pushToQueue(self,irq):
        self.queue.put(irq)

    def processInstruction(self):
        # process a instruction and trigger the interruption
        if (self.queue.qsize() > 0):
            irq = self.queue.get_nowait()
            irq.currentPcb.incrementPc()
            print(irq.instruction.text + ', pid: ' + str(irq.currentPcb.pid))
            self.interruptionManager.handle(IRQ(IRQ.EndIO, irq.currentPcb, None))



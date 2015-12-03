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
        try:
            irq = self.queue.get_nowait()
            self.lockInstructions.acquire()
            self.lockInstructions.release()
            irq.currentPcb.incrementPc()
            print(irq.instruction.text + ', pid: ' + str(irq.currentPcb.pid))
            self.interruptionManager.handle(IRQ(IRQ.EndIO, irq.currentPcb))

        except:
            pass

from queue import Queue
from threading import Thread
import time
from Code.IRQ import IRQ


class Device(Thread):

    def __init__(self, interruptionManager, memory, queue):
       Thread.__init__(self)
       self.interruptionManager= interruptionManager
       self.memory= memory
       self.queue= queue

    def pushToQueue(self,pcb):
        self.queue.put(pcb)

    def processInstruction(self):

        try:
            pcb = self.queue.get_nowait()
            instruction = self.memory.get(pcb.pc + pcb.memoryPosition)
            pcb.incrementPc()
            print(instruction.text + ', pid: ' + str(pcb.pid))
            self.interruptionManager.handle(IRQ(IRQ.EndIO, pcb))

        except:
            pass

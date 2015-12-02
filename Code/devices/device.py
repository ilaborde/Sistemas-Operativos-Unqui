from queue import Queue
from threading import Thread
import time
from Code.IRQ import IRQ


class Device(Thread):

    def __init__(self, interruptionManager, memory, queue, lockInstructions):
       Thread.__init__(self)
       self.interruptionManager= interruptionManager
       self.memory= memory
       self.queue= queue
       self.lockInstructions= lockInstructions

    def pushToQueue(self,pcb):
        self.queue.put(pcb)

    def processInstruction(self):
        # process a instruction and trigger the interruption
        try:
            pcb = self.queue.get_nowait()
            self.lockInstructions.acquire()
            instruction = self.memory.get(pcb.pc + pcb.memoryPosition)
            self.lockInstructions.release()
            pcb.incrementPc()
            print(instruction.text + ', pid: ' + str(pcb.pid))
            self.interruptionManager.handle(IRQ(IRQ.EndIO, pcb))

        except:
            pass

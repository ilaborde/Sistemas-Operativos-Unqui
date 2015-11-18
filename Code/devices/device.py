from queue import Queue
from threading import Thread
from Code.IRQ import IRQ


class Device(Thread):

    def __init__(self):
       Thread.__init__(self)

    def pushToQueue(self,pcb):
        self.queue.put(pcb)

    def processInstruction(self):
        pcb = self.queue.get()
        instruction = self.memory.get(pcb.pc + pcb.memoryPosition)
        pcb.incrementPc()
        print(instruction.text + ', pid: ' + str(pcb.pid))
        self.interruptionManager.handle(IRQ(IRQ.EndIO, pcb))

from queue import Queue
from Code.IRQ import IRQ

class Monitor:

    def __init__(self, interruptionManager, memory):
       self.queue = Queue()
       self.interruptionManager= interruptionManager
       self.memory= memory

    def pushToQueue(self,pcb):
        self.queue.put(pcb)

    def processInstruction(self):
        pcb = self.queue.get()
        instruction = self.memory.get(pcb.pc + pcb.memoryPosition)
        pcb.incrementPc()
        print(instruction.text)
        self.interruptionManager.handle(IRQ(IRQ.EndIO, pcb))

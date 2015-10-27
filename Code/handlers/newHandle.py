class NewHandle:
    def __init__(self,readyQueue):
        self.readyQueue = readyQueue
    
    def handle(self, irq):
        self.readyQueue.put(irq.currentPcb)
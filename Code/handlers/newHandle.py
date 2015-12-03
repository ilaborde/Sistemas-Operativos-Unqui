class NewHandle:
    def __init__(self, readyQueue, lock, memoryManager):
        self.readyQueue = readyQueue
        self.lock= lock
        self.memoryManager = memoryManager

    def handle(self, irq):
        self.lock.acquire()
        self.readyQueue.put(irq.currentPcb)
        self.lock.release()
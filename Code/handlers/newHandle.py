class NewHandle:
    def __init__(self, readyQueue, lock):
        self.readyQueue = readyQueue
        self.lock= lock

    def handle(self, irq):
        self.lock.acquire()
        self.readyQueue.put_nowait(irq.currentPcb)
        self.lock.release()
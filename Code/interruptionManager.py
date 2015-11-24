from threading import Thread

class InterruptionManager(Thread):
    def __init__(self, lockReadyQueue, lockIrq):
        self.handles = {}
        Thread.__init__(self)
        self.irq = None
        self.lockReadyQueue= lockReadyQueue
        self.lockIrq= lockIrq

    def registerHandler(self, irqKey, handle):
        self.handles[irqKey] = handle

    def run(self):
        Thread.run(self)

        while True:

            if (not self.irq == None):
                handler = self.handles[self.irq.type]
                if handler is not None:
                    self.lockIrq.acquire()
                    handler.handle(self.irq)
                    self.lockIrq.notifyAll()
                    self.lockIrq.release()
                    self.irq= None
                else:
                    raise ValueError("Critical error: Handle not found")

    def handle(self, irq):
         self.irq = irq


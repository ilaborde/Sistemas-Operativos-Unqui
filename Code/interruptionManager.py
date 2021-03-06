from threading import Thread
import time


class InterruptionManager(Thread):
    def __init__(self, lockReadyQueue, lockProcessing, irqQueue, lockIrqQueue):
        self.handles = {}
        Thread.__init__(self)
        self.irq = None
        self.lockReadyQueue= lockReadyQueue
        self.lockProcessing= lockProcessing
        self.lockIrqQueue= lockIrqQueue
        self.irqQueue= irqQueue

    def registerHandler(self, irqKey, handle):
        self.handles[irqKey] = handle

    def run(self):
        #handle the irq and switches to kernel mode
        Thread.run(self)

        while True:

            if (not self.irqQueue.qsize() == 0):
                self.lockProcessing.acquire()
                self.lockIrqQueue.acquire()
                irq= self.irqQueue.get_nowait()
                handler = self.handles[irq.type]
                if handler is not None:
                    handler.handle(irq)
                else:
                    raise ValueError("Critical error: Handle not found")
                self.lockIrqQueue.notifyAll()
                self.lockIrqQueue.release()
                self.lockProcessing.notifyAll()
                self.lockProcessing.release()
                time.sleep(0.2)

    def handle(self, irq):
        #add element to irqQueue
         self.irqQueue.put_nowait(irq)


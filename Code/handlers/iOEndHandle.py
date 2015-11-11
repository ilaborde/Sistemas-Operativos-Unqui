class IOEndHandle:
    def __init__(self,scheduler):
        self.scheduler= scheduler

    def handle(self, irq):
        self.scheduler.addPcbToReadyQueue(irq.currentPcb)
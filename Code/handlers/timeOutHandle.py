class TimeOutHandle:
    def __init__(self):
        pass

    def handle(self, irq):
        self.scheduler.addPcbToReadyQueue(irq.currentPcb)
        self.scheduler.currentCpu.currentPcb = None
        self.scheduler.setNextPcbToCpu()
class TimeOutHandle:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def handle(self, irq):
        self.scheduler.addPcbToReadyQueue(irq.currentPcb)
        self.scheduler.currentCpu.currentPcb = None
        self.scheduler.setNextPcbToCpu()
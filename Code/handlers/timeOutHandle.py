class TimeOutHandle:
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def handle(self, irq):
        self.scheduler.currentCpu.currentPcb = None
        self.scheduler.setNextPcbToCpu()
        self.scheduler.addPcbToReadyQueue(irq.currentPcb)
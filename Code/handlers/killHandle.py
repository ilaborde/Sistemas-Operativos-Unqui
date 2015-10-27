class KillHandle:
    def __init__(self,scheduler):
        self.scheduler = scheduler

    def handle(self, irq):
        ##TODO call to memory.free(irq.currentPcb)
        self.scheduler.currentCpu.currentPcb = None
        self.scheduler.setNextPcbToCpu()

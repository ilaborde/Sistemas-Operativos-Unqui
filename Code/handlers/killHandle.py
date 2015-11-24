class KillHandle:
    def __init__(self, scheduler, pcbTable):
        self.scheduler = scheduler
        self.pcbTable= pcbTable

    def handle(self, irq):
        ##TODO call to memory.free(irq.currentPcb)
        self.pcbTable.removepcb(self.scheduler.currentCpu.currentPcb.pid)
        self.scheduler.currentCpu.currentPcb = None
        self.scheduler.setNextPcbToCpu()

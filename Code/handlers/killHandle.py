class KillHandle:
    def __init__(self, scheduler, pcbTable, memorymanager):
        self.scheduler = scheduler
        self.pcbTable= pcbTable
        self.memoryManager = memorymanager

    def handle(self, irq):
        self.memoryManager.release(irq.currentPcb)
        self.pcbTable.removepcb(self.scheduler.currentCpu.currentPcb.pid)
        self.scheduler.currentCpu.currentPcb = None
        self.scheduler.setNextPcbToCpu()

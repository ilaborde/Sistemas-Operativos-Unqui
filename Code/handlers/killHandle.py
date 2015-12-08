class KillHandle:
    def __init__(self, scheduler, pcbTable, memorymanager):
        self.scheduler = scheduler
        self.pcbTable= pcbTable
        self.memoryManager = memorymanager

    def handle(self, irq):
        self.memoryManager.release(irq.currentPcb)
        self.pcbTable.removepcb(irq.currentCpu.currentPcb.pid)
        irq.currentCpu.currentPcb= None
        self.scheduler.setNextPcbToCpu()

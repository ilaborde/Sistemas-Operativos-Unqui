class IOHandle:
    def __init__(self,devicemanager, memory, scheduler):
        self.deviceManager = devicemanager
        self.memory = memory
        self.scheduler = scheduler

    def handle(self, irq):
        self.scheduler.currentCpu.currentPcb = None
        self.deviceManager.pushToDeviceQueue(irq)







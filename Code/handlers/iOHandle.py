class IOHandle:
    def __init__(self,devicemanager, memory, scheduler):
        self.deviceManager = devicemanager
        self.memory = memory
        self.scheduler = scheduler

    def handle(self, irq):
        irq.currentCpu.currentPcb= None
        self.deviceManager.pushToDeviceQueue(irq)







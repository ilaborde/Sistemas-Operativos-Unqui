class IOHandle:
    def __init__(self,devicemanager, memory, scheduler):
        self.deviceManager = devicemanager
        self.memory = memory
        self.scheduler = scheduler

    def handle(self, irq):
        self.scheduler.currentCpu.currentPcb = None
        self.scheduler.setNextPcbToCpu()
        instruction = self.memory.get(irq.currentPcb.pc + irq.currentPcb.memoryPosition)
        self.deviceManager.pushToDeviceQueue(instruction,irq.currentPcb)


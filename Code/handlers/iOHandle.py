class IOHandle:
    def __init__(self,devicemanager, memory):
        self.deviceManager = devicemanager
        self.memory = memory

    def handle(self, irq):
        instruction = self.memory.get(irq.currentPcb.pc + irq.currentPcb.memoryPosition)
        self.deviceManager.pushToDeviceQueue(instruction,irq.currentPcb)

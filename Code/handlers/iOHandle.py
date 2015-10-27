class IOHandle:
    # "lo manda a la cola de waiting y el IO lo procesa"
    def __init__(self,devicemanager, memory):
        self.deviceManager = devicemanager
        self.memory = memory

    def handle(self, irq):
        instruction = self.memory.get(irq.currentPcb.pc + irq.currentPcb.memoryPosition)
        self.deviceManager.pushToDeviceQueue(instruction,irq.currentPcb)

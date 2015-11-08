
class InterruptionManager:
    def __init__(self):
        self.handles = {}

    def registerHandler(self, irqKey, handle):
        self.handles[irqKey] = handle

    def handle(self, irq):
        handler = self.handles[irq.type]

        if handler is not None:
            handler.handle(irq)
        else:
            raise ValueError("Critical error: Handle not found")

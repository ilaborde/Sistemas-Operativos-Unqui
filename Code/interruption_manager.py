class KillHandle:
    # libera los recursos
    def __init__(self):
        pass

    def handle(self, irq):
        pass


class TimeOutHandle:
    # lo saca de la cpu y lo manda a la cola de ready
    def __init__(self):
        pass

    def handle(self, irq):
        pass


class IOHandle:
    # "lo manda a la cola de waiting y envia otro proceso a la cpu"
    def __init__(self):
        pass

    def handle(self, irq):
        pass


class InterruptionManager:
    def __init__(self):
        self.handles = {}

    def registry(self, irqKey, handle):
        self.handles[irqKey] = handle

    def handle(self, irq):
        handler = self.handles[irq.type]

        if handler != None:
            handler.handle(irq)
        else:
            raise ValueError("Critical error: Handle not found")

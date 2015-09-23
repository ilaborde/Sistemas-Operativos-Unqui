class IRQ:
    kill = 1
    timeOut = 2
    IO = 3

    def __init__(self, irqType, pcb):
        self.type = irqType
        self.currentPcb = pcb

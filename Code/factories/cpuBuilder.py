from Code.cpu import *

class CpuBuilder:

    def __init__(self):
        pass

    def createElement(self, memory, interruptionManager, lockpcb, irqQueue, lockIrqQueue, lockInstructions):

        cpu= Cpu(memory, interruptionManager, lockpcb, irqQueue, lockIrqQueue, lockInstructions)
        return cpu

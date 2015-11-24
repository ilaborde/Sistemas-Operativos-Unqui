from Code.cpu import *

class CpuBuilder:

    def __init__(self):
        pass

    def createElement(self, memory, interruptionManager, lockPcb):

        cpu= Cpu(memory, interruptionManager, lockPcb)
        return cpu

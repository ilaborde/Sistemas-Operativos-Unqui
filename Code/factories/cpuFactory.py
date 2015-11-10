from Code.cpu import *

class CpuFactory:

    def __init__(self):
        pass

    def createElement(self, memory, interruptionManager):

        cpu= Cpu(memory, interruptionManager)
        return cpu

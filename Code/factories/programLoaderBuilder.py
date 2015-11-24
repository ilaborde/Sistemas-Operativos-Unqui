from Code.programLoader import ProgramLoader

class ProgramLoaderBuilder:

    def __init__(self):
        pass

    def createElement(self,disk, memory, interruptionManager, pcbTable, lockIrq):
       return ProgramLoader(disk, memory, interruptionManager, pcbTable, lockIrq)


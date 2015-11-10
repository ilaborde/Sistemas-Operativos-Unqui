from Code.programLoader import ProgramLoader

class ProgramLoaderFactory:

    def __init__(self):
        pass

    def createElement(self,disk, memory, interruptionManager, pcbTable):

       return ProgramLoader(disk, memory, interruptionManager, pcbTable)


from Code.instructions import Instruction, InstructionType, ResourceType
from Code.program import Program

class Disk:
    def __init__(self):
        self.programs = {}

    def writeProgram(self, program):
        #Sets the program into the disk to store ir
        self.programs["program" + str(len(self.programs))] = program

    def getProgram(self, programName):
        return self.programs[programName]
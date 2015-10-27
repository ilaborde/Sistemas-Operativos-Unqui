from Code.instructions import Instruction, InstructionType, ResourceType
from Code.program import Program


class Disk:
    def __init__(self):
        self.programs = {}
        instruction1 = Instruction("hola", InstructionType.cpu,ResourceType.Monitor)
        program1 = Program()
        program1.add(instruction1)
        self.programs["program1"] = program1

    def getProgram(self, programName):
        return self.programs[programName]

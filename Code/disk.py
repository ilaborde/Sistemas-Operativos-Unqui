from Code.instructions import Instruction, InstructionType, ResourceType
from Code.program import Program


class Disk:
    def __init__(self):
        self.programs = {}
        instruction1 = Instruction("IO Instruction..", InstructionType.cpu, ResourceType.Monitor)
        instruction2 = Instruction("Kill Instruction.", InstructionType.kill, ResourceType.Monitor)
        program1 = Program()

        program1.add(instruction1)
        program1.add(instruction2)
        self.programs["program1"] = program1


    def getProgram(self, programName):
        return self.programs[programName]

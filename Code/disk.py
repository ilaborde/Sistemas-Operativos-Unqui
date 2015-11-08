from Code.instructions import Instruction, InstructionType, ResourceType
from Code.program import Program


class Disk:
    def __init__(self):
        self.programs = {}

        for x in range(1, 11):
            program1 = Program()
            program1.add(Instruction("Cpu Instruction..", InstructionType.cpu, ResourceType.Monitor))
            program1.add(Instruction("Kill Instruction.", InstructionType.kill, ResourceType.Monitor))
            self.programs["program" + str(x)] = program1



    def getProgram(self, programName):
        return self.programs[programName]

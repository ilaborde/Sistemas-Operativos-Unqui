from Code.disk import Disk
from Code.instructions import Instruction, InstructionType, ResourceType
from Code.program import Program


class diskFactory:

    def __init__(self):
        pass

    def createElement(self):
        return Disk()

    def configurationOfTheDiskWithTwoPrograms(self):

        program1 = Program()
        program1.add(Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction2", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("io Instruction3", InstructionType.io, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction7", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Kill Instruction", InstructionType.kill, ResourceType.Monitor))

        program2 = Program()
        program2.add(Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor))
        program2.add(Instruction("io Instruction2", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("Cpu Instruction3", InstructionType.cpu, ResourceType.Monitor))
        program2.add(Instruction("io Instruction4", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instruction5", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instruction6", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instruction7", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instruction8", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("Kill Instruction", InstructionType.kill, ResourceType.Monitor))

        Disk= self.createElement()

        Disk.writeProgram(program1)
        Disk.writeProgram(program2)

        return Disk

    def configurationOfTheDiskWithThreePrograms(self):

        program1 = Program()
        program1.add(Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction2", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("io Instruction3", InstructionType.io, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction4", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Kill Instruction", InstructionType.kill, ResourceType.Monitor))

        program2 = Program()
        program2.add(Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor))
        program2.add(Instruction("Cpu Instruction2", InstructionType.cpu, ResourceType.Monitor))
        program2.add(Instruction("io Instructio3", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio4", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio5", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio6", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio7", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio8", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("Kill Instruction", InstructionType.kill, ResourceType.Monitor))

        program3 = Program()
        program3.add(Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("Cpu Instruction2", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("io Instruction3", InstructionType.io, ResourceType.Printer))
        program3.add(Instruction("Cpu Instruction4", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("Cpu Instruction5", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("Cpu Instruction6", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("io Instructio7", InstructionType.io, ResourceType.Printer))
        program3.add(Instruction("io Instructio8", InstructionType.io, ResourceType.Printer))
        program3.add(Instruction("Kill Instruction", InstructionType.kill, ResourceType.Monitor))

        Disk= self.createElement()

        Disk.writeProgram(program1)
        Disk.writeProgram(program2)
        Disk.writeProgram(program3)

        return Disk
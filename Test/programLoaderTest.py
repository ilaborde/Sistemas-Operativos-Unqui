from queue import Queue
from threading import Condition
import unittest
from unittest.mock import Mock
from Code.IRQ import IRQ
from Code.disk import Disk
from Code.instructions import Instruction, InstructionType, ResourceType
from Code.interruptionManager import InterruptionManager
from Code.memory import Memory
from Code.memoryManager import MemoryManager
from Code.pcbTable import PcbTable
from Code.program import Program
from Code.programLoader import ProgramLoader


class TestsProgramLoader(unittest.TestCase):

    def setUp(self):
        self.disk= Disk()
        self.irqQueueMock =Queue()
        self.killHandleMock = Mock()
        self.timeOutHandleMock = Mock()
        self.ioHandleMock = Mock()

        self.lockProcessingMock= Condition()
        self.lockIrqQueueMock = Condition()
        self.lockReadyQueueMock= Condition()
        self.lockInstructions= Condition()
        self.lockIrq= Condition()
        self.memory= Memory(self.lockInstructions)

        self.interruptionManager = InterruptionManager(self.lockReadyQueueMock,self.lockProcessingMock, self.irqQueueMock, self.lockIrqQueueMock)
        self.interruptionManager.registerHandler(IRQ.kill, self.killHandleMock)
        self.interruptionManager.registerHandler(IRQ.timeOut, self.timeOutHandleMock)
        self.interruptionManager.registerHandler(IRQ.IO, self.ioHandleMock)
        self.programLoader= ProgramLoader(self.disk, self.memory, self.interruptionManager, PcbTable(), self.lockIrq)
        self.memoryManager= MemoryManager(self.memory, self.disk)

    def test_when_have_a_program_Then_I_want_to_create_a_pcb_with_pid_1(self):

        program= Program()
        self.assertEqual(self.programLoader.createPcb(program, "program0").pid, 1)

    def test_when_have_a_program_Then_the_memory_is_write_with_a_new_program(self):

        program= Program()
        instruction1= Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor)
        instruction2= Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor)
        instruction3= Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor)
        instruction4= Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor)
        program.add(instruction1)
        program.add(instruction2)
        program.add(instruction3)
        program.add(instruction4)
        self.memoryManager.loadToMemory(self.programLoader.createPcb(program,"program0"), program.instructions)
        self.assertEqual(self.memory.cells[1], instruction2)




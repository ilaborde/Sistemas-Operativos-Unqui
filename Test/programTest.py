from queue import Queue
from threading import Condition
import unittest
from unittest.mock import Mock
from Code.IRQ import IRQ
from Code.disk import Disk
from Code.instructions import Instruction, InstructionType, ResourceType
from Code.interruptionManager import InterruptionManager
from Code.memory import Memory
from Code.pcbTable import PcbTable
from Code.program import Program
from Code.programLoader import ProgramLoader


class TestsProgram(unittest.TestCase):

    def setUp(self):
        pass

    def test_when_have_a_program_Then_I_want_to_add_a_two_instructions(self):
        program= Program()
        program.add(Mock())
        program.add(Mock())
        self.assertEqual(len(program.instructions), 2)


import unittest
from unittest.mock import Mock, MagicMock

from Code.IRQ import IRQ
from Code.cpu import Cpu
from Code.instructions import Instruction
from Code.interruption_manager import InterruptionManager, KillHandle, IOHandle, TimeOutHandle
from Code.memory import Memory
from Code.pcb import Pcb


class TestsCpu(unittest.TestCase):
    def setUp(self):
        instruction = Instruction("",Instruction.cpu)
        memory = Memory()
        initialPosition = memory.put([instruction])

        interruptionManager = InterruptionManager()
        killMock = MagicMock(KillHandle())
        killMock.handle.side_effect = Exception("Critical error: Handle not found")
        interruptionManager.registry(IRQ.kill, killMock)
        interruptionManager.registry(IRQ.timeOut,  Mock(TimeOutHandle()))
        interruptionManager.registry(IRQ.IO,  Mock(IOHandle()))

        pcb = Pcb(initialPosition, 1)
        self.cpu = Cpu(memory,interruptionManager)
        self.cpu.setPcb(pcb)
    # def test_ProgramInstructionsLen(self):
    # self.assertEqual(self.program.instructionsSize(), 1, "Incorrect size")

    ##def test_can_do_fetch(self):
      ##   self.cpu.fetch()

    def test_can_handle_kill(self):
        self.fail(self.cpu.fetch(),"Critical error: Handle not found")
    #
    # def test_can_handle_IO(self):
    #     pass
    #
    # def test_can_handle_timeOut(self):
    #     pass


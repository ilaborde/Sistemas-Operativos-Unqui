import unittest
from unittest.mock import Mock

from Code.IRQ import IRQ
from Code.cpu import Cpu
from Code.instructions import Instruction
from Code.memory import Memory
from Code.pcb import Pcb
from Test.matcher import Matcher


class TestsCpu(unittest.TestCase):
    def setUp(self):
        self.memory = Memory()
        self.interruptionManagerMock = Mock()
        self.cpu = Cpu(self.memory, self.interruptionManagerMock)

    def test_fetch_end_of_program(self):
        pcbFinished = Pcb(0, 0)
        self.cpu.setPcb(pcbFinished)
        self.cpu.fetch()
        irq = IRQ(IRQ.kill, pcbFinished)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

    def test_fetch_handle_IO(self):
        instruction = Instruction("", Instruction.io)
        self.memory.put([instruction])
        pcbterminado = Pcb(0, 1)
        self.cpu.setPcb(pcbterminado)
        self.cpu.fetch()
        irq = IRQ(IRQ.IO, pcbterminado)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

        # def test_can_handle_timeOut(self):
        #     pass

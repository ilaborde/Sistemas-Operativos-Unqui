import unittest
from unittest.mock import Mock

from Code.IRQ import IRQ
from Code.cpu import Cpu
from Code.instructions import Instruction, ResourceType, InstructionType
from Code.memory import Memory
from Code.pcb import Pcb
from Test.Matcher import Matcher


class TestsCpu(unittest.TestCase):
    def setUp(self):
        self.LockInstructionMock= Mock()
        self.memory = Memory(self.LockInstructionMock)
        self.interruptionManagerMock = Mock()
        self.quantum = 1
        self.lockPcbMock =Mock()
        self.irqQueueMock =Mock()
        self.lockIrqQueueMock = Mock()
        self.cpu = Cpu(self.memory, self.interruptionManagerMock, self.lockPcbMock, self.irqQueueMock, self.lockIrqQueueMock)

    def test_when_fetch_end_of_program_then_call_kill_handler(self):
        instruction = Instruction("", InstructionType.kill, ResourceType.Monitor)
        self.memory.put([instruction])
        pcbfinished = Pcb(0, 0, 1)
        self.cpu.setPcb(pcbfinished, self.quantum)
        self.cpu.fetch()
        irq = IRQ(IRQ.kill, pcbfinished)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

    def test_when_fetch_io_instruction_then_call_handle_io(self):
        instruction = Instruction("", InstructionType.io, ResourceType.Monitor)
        self.memory.put([instruction])
        pcb = Pcb(0, 1, 1)
        self.cpu.setPcb(pcb, self.quantum)
        self.cpu.fetch()
        irq = IRQ(IRQ.IO, pcb)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

    def test_when_fetch_quantum_equal_zero_then_call_time_out(self):
        pcb = Pcb(0, 0, 0)
        self.quantum = 0
        self.cpu.setPcb(pcb, self.quantum)
        self.cpu.fetch()
        irq = IRQ(IRQ.timeOut, pcb)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

    def test_when_fetch_quantum_decreases_to_zero_then_call_time_out(self):
        instruction = Instruction("", InstructionType.cpu, ResourceType.Monitor)
        instruction2 = Instruction("", InstructionType.cpu, ResourceType.Monitor)
        self.memory.put([instruction, instruction2])
        pcb = Pcb(0, 2, 2)
        self.cpu.setPcb(pcb, self.quantum)
        self.cpu.fetch()
        irq = IRQ(IRQ.timeOut, pcb)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

from queue import Queue
import unittest
from unittest.mock import Mock

from Code.IRQ import IRQ
from Code.cpu import Cpu
from Code.disk import Disk
from Code.factories.framesFactory import FramesFactory
from Code.instructions import Instruction, ResourceType, InstructionType
from Code.memory import Memory
from Code.memoryManager import MemoryManager
from Code.pcb import Pcb
from Code.swapDisk import SwapDisk
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
        self.disk= Disk()
        self.frames= FramesFactory().createElement(16)
        self.swapDisk= SwapDisk()
        self.memoryManager= MemoryManager(self.memory,self.disk, self.swapDisk,self.frames)
        self.cpu = Cpu(self.memoryManager, self.interruptionManagerMock, self.lockPcbMock, self.irqQueueMock, self.lockIrqQueueMock, Mock(),'1')

    def test_when_fetch_end_of_program_then_call_kill_handler(self):
        queueInstruction= Queue()
        instruction = Instruction("", InstructionType.kill, ResourceType.Monitor)
        pcbfinished = Pcb(0, 0, 1)
        queueInstruction.put(instruction)
        self.memoryManager.loadToMemory(pcbfinished, queueInstruction)
        self.cpu.setPcb(pcbfinished, self.quantum)
        self.cpu.fetch()
        irq = IRQ(IRQ.kill, pcbfinished, self.memoryManager,self.cpu)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

    def test_when_fetch_io_instruction_then_call_handle_io(self):
        queueInstruction= Queue()
        instruction = Instruction("", InstructionType.io, ResourceType.Monitor)
        pcb = Pcb(0, 0, 1)
        queueInstruction.put(instruction)
        self.memoryManager.loadToMemory(pcb, queueInstruction)
        self.cpu.setPcb(pcb, self.quantum)
        self.cpu.fetch()
        irq = IRQ(IRQ.IO, pcb, instruction,self.cpu)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))

    def test_when_fetch_quantum_equal_zero_then_call_time_out(self):
        pcb = Pcb(0, 0, 0)
        self.quantum = 0
        self.cpu.setPcb(pcb, self.quantum)
        self.cpu.fetch()
        irq = IRQ(IRQ.timeOut, pcb, None,self.cpu)
        self.interruptionManagerMock.handle.assert_called_with(Matcher(irq))


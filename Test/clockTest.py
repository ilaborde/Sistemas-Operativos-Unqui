import unittest
from unittest.mock import Mock

from Code.clock import Clock
from Code.cpu import Cpu


class TestsClock(unittest.TestCase):
    def setUp(self):
        pass

    def test_when_registry_cpu_then_verify_registry_list_is_incremented(self):
        self.memory = Mock()
        self.interruptionManagerMock = Mock()
        cpu = Cpu(self.memory, self.interruptionManagerMock)

        clock = Clock()
        clock.registrycpu(cpu)
        self.assertEqual(len(clock.cpuList), 1)

    def test_when_tick_then_call_cpu_fetch(self):
        cpu = Mock()
        clock = Clock()
        clock.registrycpu(cpu)
        clock.tick()
        self.assertEqual(cpu.fetch.called, True)

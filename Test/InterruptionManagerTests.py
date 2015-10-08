import unittest
from unittest.mock import Mock
from Code.IRQ import IRQ
from Code.interruption_manager import InterruptionManager
from Code.pcb import Pcb


class InterruptionManagerTests(unittest.TestCase):
    def setUp(self):
        self.killHandleMock = Mock()
        self.timeOutHandleMock = Mock()
        self.ioHandleMock = Mock()

        self.interruptionManager = InterruptionManager()
        self.interruptionManager.registry(IRQ.kill, self.killHandleMock)
        self.interruptionManager.registry(IRQ.timeOut, self.timeOutHandleMock)
        self.interruptionManager.registry(IRQ.IO, self.ioHandleMock)

    def test_registry(self):
        self.assertEqual(len(self.interruptionManager.handles), 3)

    def testCanHandleKILL(self):
        irq = IRQ(IRQ.kill, Pcb(0, 0))
        self.interruptionManager.handle(irq)
        self.killHandleMock.handle.assert_called_with(irq)
        self.assertEqual(self.ioHandleMock.call_count, 0)
        self.assertEqual(self.timeOutHandleMock.call_count, 0)

    def testCanHandleTIMEOUT(self):
        irq = IRQ(IRQ.timeOut, Pcb(0, 0))
        self.interruptionManager.handle(irq)
        self.timeOutHandleMock.handle.assert_called_with(irq)
        self.assertEqual(self.ioHandleMock.call_count, 0)
        self.assertEqual(self.killHandleMock.call_count, 0)

    def testCanHandleIO(self):
        irq = IRQ(IRQ.IO, Pcb(0, 0))
        self.interruptionManager.handle(irq)
        self.ioHandleMock.handle.assert_called_with(irq)
        self.assertEqual(self.killHandleMock.call_count, 0)
        self.assertEqual(self.timeOutHandleMock.call_count, 0)

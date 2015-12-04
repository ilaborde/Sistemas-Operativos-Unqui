from queue import Queue
from threading import Condition
import unittest
from unittest.mock import Mock
from Code.IRQ import IRQ
from Code.interruptionManager import InterruptionManager
from Code.pcb import Pcb


class InterruptionManagerTests(unittest.TestCase):
    def setUp(self):
        self.killHandleMock = Mock()
        self.timeOutHandleMock = Mock()
        self.ioHandleMock = Mock()

        self.lockProcessingMock= Condition()
        self.irqQueueMock =Queue()
        self.lockIrqQueueMock = Condition()
        self.lockReadyQueueMock= Condition()

        self.interruptionManager = InterruptionManager(self.lockReadyQueueMock,self.lockProcessingMock, self.irqQueueMock, self.lockIrqQueueMock)
        self.interruptionManager.registerHandler(IRQ.kill, self.killHandleMock)
        self.interruptionManager.registerHandler(IRQ.timeOut, self.timeOutHandleMock)
        self.interruptionManager.registerHandler(IRQ.IO, self.ioHandleMock)


    def test_registry(self):
        self.assertEqual(len(self.interruptionManager.handles), 3)

    def testCanHandleKILL(self):
        self.interruptionManager.setDaemon(True)
        irq = IRQ(IRQ.kill, Pcb(0, 0, 0), None)
        self.interruptionManager.handle(irq)
        self.interruptionManager.start()
        self.killHandleMock.handle.assert_called_with(irq)
        self.assertEqual(self.ioHandleMock.call_count, 0)
        self.assertEqual(self.timeOutHandleMock.call_count, 0)

    def testCanHandleTIMEOUT(self):
        self.interruptionManager.setDaemon(True)
        irq = IRQ(IRQ.timeOut, Pcb(0, 0, 0), None)
        self.interruptionManager.handle(irq)
        self.interruptionManager.start()
        self.timeOutHandleMock.handle.assert_called_with(irq)
        self.assertEqual(self.ioHandleMock.call_count, 0)
        self.assertEqual(self.killHandleMock.call_count, 0)

    def testCanHandleIO(self):
        self.interruptionManager.setDaemon(True)
        irq = IRQ(IRQ.IO, Pcb(0, 0, 1), None)
        self.interruptionManager.handle(irq)
        self.interruptionManager.start()
        self.ioHandleMock.handle.assert_called_with(irq)
        self.assertEqual(self.killHandleMock.call_count, 0)
        self.assertEqual(self.timeOutHandleMock.call_count, 0)

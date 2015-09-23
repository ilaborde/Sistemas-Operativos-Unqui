import unittest
from Code.IRQ import IRQ
from Code.interruption_manager import InterruptionManager, KillHandle, TimeOutHandle, IOHandle


class InterruptionManagerTests(unittest.TestCase):
    def setUp(self):
        self.interruptionManager1 = InterruptionManager()
        self.killHandle = KillHandle()
        self.timeOutHandle = TimeOutHandle()
        self.ioHandle = IOHandle()

    def testCanResgistryHandle(self):
        # "interruptionManager have two handles and the value expected of the handles list length is 2
        self.interruptionManager1.registry(IRQ.timeOut, self.timeOutHandle)
        self.interruptionManager1.registry(IRQ.IO, self.ioHandle)

        self.assertEqual(len(self.interruptionManager1.handles), 2)

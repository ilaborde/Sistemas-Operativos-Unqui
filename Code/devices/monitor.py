from queue import Queue
from threading import Thread
import time
from Code.devices.device import Device


class Monitor(Device):

    def __init__(self, interruptionManager, memory, lockInstructions):
       Device.__init__(self, interruptionManager, memory, Queue(), lockInstructions)
       Thread.__init__(self)

    def run(self):
        Thread.run(self)
        while True:
           self.processInstruction()






from queue import Queue
from threading import Thread
import time
from Code.devices.device import Device


class Printer(Device):

    def __init__(self, interruptionManager, lockInstructions):
       Device.__init__(self, interruptionManager, Queue(), lockInstructions)
       Thread.__init__(self)

    def run(self):
        Thread.run(self)
        while True:
            self.processInstruction()





from queue import Queue
from threading import Thread
from Code.devices.device import Device


class Printer(Device):

    def __init__(self, interruptionManager, memory):
       self.interruptionManager= interruptionManager
       self.memory= memory
       self.queue = Queue()
       Thread.__init__(self)

    def run(self):
        Thread.run(self)

        while True:
          if (self.queue._qsize() > 0):
            self.processInstruction()
            print ("Printer is processing..")



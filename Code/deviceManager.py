from threading import Thread
import time
from Code.instructions import InstructionType


class DeviceManager(Thread):
    def __init__(self):
        self.devices = {}
        self.irqToQueue= None
        self.currentDevice= None
        Thread.__init__(self)

    def registerDevice(self, resourceType, device):
        #Registry devices into the device manager like a monitor, printer, etc
        self.devices[resourceType] = device
        return self

    def run(self):
        Thread.run(self)

        while True:

            if(not self.irqToQueue == None):
                self.currentDevice.pushToQueue(self.irqToQueue)
                self.irqToQueue= None

    def pushToDeviceQueue(self,irq):

        device = self.devices[irq.instruction.resourceType]
        if device is not None:
            self.irqToQueue= irq
            self.currentDevice= device
        else:
            raise ValueError("Critical error: Device not found")

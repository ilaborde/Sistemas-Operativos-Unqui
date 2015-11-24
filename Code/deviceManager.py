from threading import Thread
from Code.instructions import InstructionType


class DeviceManager(Thread):
    def __init__(self):
        self.devices = {}
        self.pcbToQueue= None
        self.currentDevice= None
        Thread.__init__(self)

    def registerDevice(self, resourceType, device):
        self.devices[resourceType] = device
        return self

    def run(self):
        Thread.run(self)

        while True:

            if(not self.pcbToQueue == None):
                self.currentDevice.pushToQueue(self.pcbToQueue)
                self.pcbToQueue= None

    def pushToDeviceQueue(self, instruction, pcb):

        device = self.devices[instruction.resourceType]
        if device is not None:
            self.pcbToQueue= pcb
            self.currentDevice= device
        else:
            raise ValueError("Critical error: Device not found")


class DeviceManager:
    def __init__(self):
        self.devices = {}

    def registerDevice(self, resourceType, device):
        self.devices[resourceType] = device

    def pushToDeviceQueue(self, instruction, pcb):
        device = self.devices[instruction.resourceType]

        if device is not None:
            device.pushToQueue(pcb)
            device.processInstruction()
        else:
            raise ValueError("Critical error: Handle not found")

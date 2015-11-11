from Code.deviceManager import DeviceManager


class DeviceManagerFactory:

    def __init__(self):
        pass

    def createElement(self, resourceType, device):
        return DeviceManager().registerDevice(resourceType,device)





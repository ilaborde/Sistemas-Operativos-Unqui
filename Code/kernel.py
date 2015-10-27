from queue import Queue
from Code.clock import Clock
from Code.deviceManager import DeviceManager
from Code.devices.monitor import Monitor
from Code.disk import Disk
from Code.handlers.iOHandle import IOHandle
from Code.handlers.killHandle import KillHandle
from Code.handlers.newHandle import NewHandle
from Code.handlers.timeOutHandle import TimeOutHandle
from Code.instructions import ResourceType
from Code.programLoader import ProgramLoader
from Code.scheduler import Scheduler
from Code.cpu import *
from Code.interruption_manager import *
from Code.memory import Memory


class Kernel:
    def __init__(self):
        self.setup()

    def setup(self):
        self.memory = Memory()
        self.interruptionManager1 = InterruptionManager()
        self.cpu = Cpu(self.memory, self.interruptionManager1)
        self.clock = Clock()
        self.clock.registrycpu(self.cpu)
        self.readyQueue= Queue()
        self.scheduler= Scheduler(self.cpu,self.readyQueue)
        self.disk = Disk()
        self.deviceManager = DeviceManager()
        self.deviceManager.registryDevice(ResourceType.Monitor,Monitor())
        self.interruptionManager1.registry(IRQ.kill, KillHandle(self.scheduler))
        self.interruptionManager1.registry(IRQ.timeOut, TimeOutHandle())
        self.interruptionManager1.registry(IRQ.IO, IOHandle(self.deviceManager))
        self.interruptionManager1.registry(IRQ.New, NewHandle(self.readyQueue))
        self.programLoader = ProgramLoader(self.disk,self.memory, self.interruptionManager1)

    def run(self):
        self.programLoader.load("program1")
        self.scheduler.setNextPcbToCpu()
        self.clock.tick()
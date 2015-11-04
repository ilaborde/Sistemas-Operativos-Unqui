from queue import Queue
from Code.clock import Clock
from Code.deviceManager import DeviceManager
from Code.devices.monitor import Monitor
from Code.disk import Disk
from Code.handlers.iOHandle import IOHandle
from Code.handlers.killHandle import KillHandle
from Code.handlers.iOEndHandle import IOEndHandle
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
        self.interruptionManager = InterruptionManager()
        self.clock = Clock()
        self.readyQueue = Queue()
        self.disk = Disk()
        self.deviceManager = DeviceManager()

        self.cpu = Cpu(self.memory, self.interruptionManager)
        self.clock.registrycpu(self.cpu)
        self.scheduler = Scheduler(self.cpu,self.readyQueue, 3)

        self.deviceManager.registerDevice(ResourceType.Monitor,Monitor(self.interruptionManager, self.memory))

        self.interruptionManager.registerHandler(IRQ.kill, KillHandle(self.scheduler))
        self.interruptionManager.registerHandler(IRQ.timeOut, TimeOutHandle())
        self.interruptionManager.registerHandler(IRQ.IO, IOHandle(self.deviceManager, self.memory))
        self.interruptionManager.registerHandler(IRQ.EndIO, IOEndHandle(self.scheduler))
        self.interruptionManager.registerHandler(IRQ.New, NewHandle(self.readyQueue))

        self.programLoader = ProgramLoader(self.disk, self.memory, self.interruptionManager)

    def run(self):
        self.programLoader.load("program1")
        self.scheduler.setNextPcbToCpu()
        self.clock.tick()
        self.clock.tick()
        self.clock.tick()

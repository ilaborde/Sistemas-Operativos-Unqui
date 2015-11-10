from Code import IRQ
from Code.handlers.iOEndHandle import IOEndHandle
from Code.handlers.iOHandle import IOHandle
from Code.handlers.killHandle import KillHandle
from Code.handlers.newHandle import NewHandle
from Code.handlers.timeOutHandle import TimeOutHandle
from Code.interruptionManager import InterruptionManager


class interruptionManagerFactory:

    def __init__(self):
        pass

    def createElement(self):

       return InterruptionManager()

    def registryInterruptionManager(self, interruptionManager, deviceManager, scheduler, memory, readyQueue):

        interruptionManager.registerHandler(IRQ.IRQ.kill, KillHandle(scheduler))
        interruptionManager.registerHandler(IRQ.IRQ.timeOut, TimeOutHandle())
        interruptionManager.registerHandler(IRQ.IRQ.IO, IOHandle(deviceManager, memory))
        interruptionManager.registerHandler(IRQ.IRQ.EndIO, IOEndHandle(scheduler))
        interruptionManager.registerHandler(IRQ.IRQ.New, NewHandle(readyQueue))



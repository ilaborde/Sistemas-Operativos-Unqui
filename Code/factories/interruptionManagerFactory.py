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

    def registryInterruptionManager(self, interruptionmanager, devicenanager, scheduler, memory, readyqueue):
        interruptionmanager.registerHandler(IRQ.IRQ.kill, KillHandle(scheduler))
        interruptionmanager.registerHandler(IRQ.IRQ.timeOut, TimeOutHandle(scheduler))
        interruptionmanager.registerHandler(IRQ.IRQ.IO, IOHandle(devicenanager, memory, scheduler))
        interruptionmanager.registerHandler(IRQ.IRQ.EndIO, IOEndHandle(scheduler))
        interruptionmanager.registerHandler(IRQ.IRQ.New, NewHandle(readyqueue))

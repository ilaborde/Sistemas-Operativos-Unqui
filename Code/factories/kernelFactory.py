from queue import Queue
from threading import Lock, RLock, Condition
from Code.devices.printer import Printer
from Code.factories.clockBuilder import ClockBuilder
from Code.factories.cpuBuilder import CpuBuilder
from Code.factories.deviceManagerBuilder import DeviceManagerBuilder
from Code.factories.diskFactory import diskFactory
from Code.factories.memoryFactory import MemoryFactory
from Code.factories.programLoaderBuilder import ProgramLoaderBuilder
from Code.factories.schedulerBuilder import SchedulerBuilder
from Code.devices.monitor import Monitor
from Code.instructions import ResourceType, Instruction, InstructionType
from Code.kernel import Kernel
from Code.memoryManager import MemoryManager
from Code.pcbTable import PcbTable
from Code.program import Program
from Code.factories.interruptionManagerBuilder import interruptionManagerBuilder


class kernelFactory:
    def __init__(self):
        pass

    def selectConfiguration(self, option):
        if (option == 1):
            return self.configurationOne()

    def configurationOne(self):
        # create some configuration for kernel

        lockReadyQueue = Condition()
        lockInstructions = Condition()
        lockPcb = Condition()
        pcbTable = PcbTable()
        irqQueue = Queue()
        lockIrqQueue = Condition()
        lockProcessing = Condition()

        InterruptionManagerBuilder = interruptionManagerBuilder()
        readyQueue = Queue()
        disk = diskFactory().configurationOfTheDiskWithThreePrograms()

        memory = MemoryFactory().createElement(lockInstructions)
        memoryManager = MemoryManager(memory,disk)
        interruptionManager = InterruptionManagerBuilder.createElement(lockReadyQueue, lockProcessing, irqQueue,
                                                                       lockIrqQueue)

        cpu = CpuBuilder().createElement(memoryManager, interruptionManager, lockPcb, irqQueue, lockIrqQueue, lockInstructions)
        scheduler = SchedulerBuilder().createElement(cpu, readyQueue, 4, lockReadyQueue)
        ##todo remove memory
        monitorDevice = Monitor(interruptionManager, lockInstructions)
        printerDevice = Printer(interruptionManager, lockInstructions)
        monitorDevice.start()
        printerDevice.start()

        deviceManager = DeviceManagerBuilder().createElement(ResourceType.Monitor, monitorDevice)
        deviceManager.registerDevice(ResourceType.Printer, printerDevice)
        InterruptionManagerBuilder.registryInterruptionManager(interruptionManager, deviceManager, scheduler,
                                                               memoryManager,
                                                               readyQueue, lockReadyQueue, pcbTable)

        interruptionManager.start()
        clock = ClockBuilder().createElement(cpu, lockProcessing)

        programLoader = ProgramLoaderBuilder().createElement(disk, memoryManager, interruptionManager, pcbTable, lockIrqQueue)

        clock.setDaemon(True)

        clock.start()
        deviceManager.start()
        kernel = Kernel()
        kernel.initializeKernel(clock, programLoader, scheduler)
        kernel.start()
        return kernel

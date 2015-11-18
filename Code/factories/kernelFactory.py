from queue import Queue
from Code.devices.printer import Printer
from Code.factories.clockFactory import ClockFactory
from Code.factories.cpuFactory import CpuFactory
from Code.factories.deviceManagerFactory import DeviceManagerFactory
from Code.factories.diskFactory import diskFactory
from Code.factories.memoryFactory import MemoryFactory
from Code.factories.programLoaderFactory import ProgramLoaderFactory
from Code.factories.schedulerFactory import SchedulerFactory
from Code.devices.monitor import Monitor
from Code.instructions import ResourceType, Instruction, InstructionType
from Code.kernel import Kernel
from Code.pcbTable import PcbTable
from Code.program import Program
from Code.factories.interruptionManagerFactory import interruptionManagerFactory


class kernelFactory:
    def __init__(self):
        pass

    def selectConfiguration(self, option):
        if (option == 1):
            return self.configurationOne()

    def configurationOne(self):
        program1 = Program()
        program1.add(Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Io Instruction2", InstructionType.io, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction3", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Io Instruction4", InstructionType.io, ResourceType.Printer))
        program1.add(Instruction("Io Instruction5", InstructionType.io, ResourceType.Printer))
        program1.add(Instruction("Kill Instruction.", InstructionType.kill, ResourceType.Monitor))

        program2 = Program()
        program2.add(Instruction("Cpu Instruction1..", InstructionType.cpu, ResourceType.Monitor))
        program2.add(Instruction("Io Instruction2", InstructionType.io, ResourceType.Printer))
        program1.add(Instruction("Io Instruction3", InstructionType.io, ResourceType.Printer))
        program1.add(Instruction("Io Instruction4", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("Io Instruction5", InstructionType.io, ResourceType.Monitor))
        program2.add(Instruction("Cpu Instruction6..", InstructionType.cpu, ResourceType.Monitor))
        program2.add(Instruction("Kill Instruction.", InstructionType.kill, ResourceType.Monitor))

        InterruptionManagerFactory = interruptionManagerFactory()
        readyQueue = Queue()
        disk = diskFactory().createElement()
        disk.writeProgram(program1)
        disk.writeProgram(program2)

        memory = MemoryFactory().createElement()
        interruptionManager = InterruptionManagerFactory.createElement()
        cpu = CpuFactory().createElement(memory, interruptionManager)
        scheduler = SchedulerFactory().createElement(cpu, readyQueue, 2)
        monitorDevice= Monitor(interruptionManager, memory)
        printerDevice = Printer(interruptionManager, memory )
        monitorDevice.start()
        printerDevice.start()

        deviceManager = DeviceManagerFactory().createElement(ResourceType.Monitor, monitorDevice)
        deviceManager.registerDevice(ResourceType.Printer, printerDevice)
        InterruptionManagerFactory.registryInterruptionManager(interruptionManager, deviceManager, scheduler, memory,
                                                               readyQueue)
        clock = ClockFactory().createElement(cpu)
        programLoader = ProgramLoaderFactory().createElement(disk, memory, interruptionManager, PcbTable())

        kernel = Kernel()
        kernel.initializeKernel(clock, programLoader, scheduler)

        return kernel

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
        lockReadyQueue= Condition()
        lockInstructions= Condition()
        lockIrq= Condition()
        lockPcb= Condition()
        pcbTable= PcbTable()

        program1 = Program()
        program1.add(Instruction("Cpu Instruction1", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction3", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction4", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program1.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program1.add(Instruction("Cpu Instruction6", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Cpu Instruction7", InstructionType.cpu, ResourceType.Monitor))
        program1.add(Instruction("Kill Instruction.", InstructionType.kill, ResourceType.Monitor))

        program2 = Program()
        program2.add(Instruction("Cpu Instruction1..", InstructionType.cpu, ResourceType.Monitor))

        program2.add(Instruction("Cpu Instruction2..", InstructionType.cpu, ResourceType.Monitor))
        program2.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program2.add(Instruction("Kill Instruction7.", InstructionType.kill, ResourceType.Monitor))

        program3 = Program()
        program3.add(Instruction("Cpu Instruction1..", InstructionType.cpu, ResourceType.Monitor))

        program3.add(Instruction("Cpu Instruction2..", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("Cpu Instruction3", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("Cpu Instruction4", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("Cpu Instruction5..", InstructionType.cpu, ResourceType.Monitor))
        program3.add(Instruction("io Instructio7.", InstructionType.io, ResourceType.Printer))
        program3.add(Instruction("io Instructio8.", InstructionType.io, ResourceType.Printer))
        program3.add(Instruction("io Instructio9.", InstructionType.io, ResourceType.Printer))
        program3.add(Instruction("Kill Instruction7.", InstructionType.kill, ResourceType.Monitor))

        InterruptionManagerBuilder = interruptionManagerBuilder()
        readyQueue = Queue()
        disk = diskFactory().createElement()
        disk.writeProgram(program1)
        disk.writeProgram(program2)
        disk.writeProgram(program3)

        memory = MemoryFactory().createElement(lockInstructions)
        interruptionManager = InterruptionManagerBuilder.createElement(lockReadyQueue, lockIrq)

        cpu = CpuBuilder().createElement(memory, interruptionManager, lockPcb)
        scheduler = SchedulerBuilder().createElement(cpu, readyQueue, 2, lockReadyQueue)
        monitorDevice= Monitor(interruptionManager, memory)
        printerDevice = Printer(interruptionManager, memory )
        monitorDevice.start()
        printerDevice.start()

        deviceManager = DeviceManagerBuilder().createElement(ResourceType.Monitor, monitorDevice)
        deviceManager.registerDevice(ResourceType.Printer, printerDevice)
        InterruptionManagerBuilder.registryInterruptionManager(interruptionManager, deviceManager, scheduler, memory,
                                                               readyQueue, lockReadyQueue, pcbTable)
        interruptionManager.start()
        clock = ClockBuilder().createElement(cpu)
        programLoader = ProgramLoaderBuilder().createElement(disk, memory, interruptionManager,pcbTable , lockIrq)
        clock.start()
        deviceManager.start()
        kernel = Kernel()
        kernel.initializeKernel(clock, programLoader, scheduler)
        kernel.start()
        return kernel

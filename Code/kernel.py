from queue import Queue
from Code.clock import Clock
from Code.handlers.iOHandle import IOHandle
from Code.handlers.killHandle import KillHandle
from Code.handlers.timeOutHandle import TimeOutHandle
from Code.scheduler import Scheduler
from Code.cpu import *
from Code.interruption_manager import *
from Code.memory import Memory
from Code.pcb import Pcb
from Code.program import Program


class Kernel:
    def __init__(self):
        self.setup()

    def setup(self):
        self.memory = Memory()
        self.interruptionManager1 = InterruptionManager()
        self.cpu = Cpu(self.memory, self.interruptionManager1)
        self.clock = Clock()
        self.clock.registrycpu(self.cpu)
        self.scheduler= Scheduler(self.cpu)
        self.interruptionManager1.registry(IRQ.kill, KillHandle(self.scheduler))
        self.interruptionManager1.registry(IRQ.timeOut, TimeOutHandle())
        self.interruptionManager1.registry(IRQ.IO, IOHandle())

    def run(self):
        readyQueue= Queue()
        instruction = Instruction("hola", Instruction.cpu)
        program = Program()  # TODO: class disco
        program.add(instruction)
        initialPosition = self.memory.put(program.instructions)
        pcb = Pcb(initialPosition, len(program.instructions))
        readyQueue.put(pcb)
        self.scheduler.setReadyQueue(readyQueue)
        self.scheduler.putPcb()
        self.clock.tick()

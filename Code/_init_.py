from Code import IRQ
from Code.Clock import Clock
from Code.cpu import *
from Code.interruption_manager import *
from Code.memory import Memory
from Code.pcb import Pcb
from Code.program import Program

if __name__ == '__main__':
    instruction = Instruction("hola", Instruction.cpu)

    program = Program()
    program.add(instruction)

    memory = Memory()
    interruptionManager1 = InterruptionManager()

    interruptionManager1.registry(IRQ.kill, KillHandle())
    interruptionManager1.registry(IRQ.timeOut, TimeOutHandle())
    interruptionManager1.registry(IRQ.IO, IOHandle())

    cpu = Cpu(memory, interruptionManager1)
    initialPosition = memory.put(program.instructions)

    pcb = Pcb(initialPosition, len(program.instructions))

    clock = Clock()
    clock.registrycpu(cpu)
    cpu.setPcb(pcb)

    clock.tick()
    # clock.tick()
    # clock.tick()

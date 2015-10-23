from Code import IRQ
from Code.clock import Clock
from Code.kernel import Kernel
from Code.cpu import *
from Code.interruption_manager import *
from Code.memory import Memory
from Code.pcb import Pcb
from Code.program import Program

if __name__ == '__main__':

    kernel= Kernel()
    kernel.run()
class Pcb:

    def __init__(self, position, pid, count):
        self.pc = 0
        self.pid = pid
        self.memoryPosition = position
        self.programLength = count
    
    def incrementPc(self):
        #Increment program counter in order to goes to the next instruction of the program
        self.pc += 1


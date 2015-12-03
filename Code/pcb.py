class Pcb:

    def __init__(self, pid, length, programname):
        self.pc = 0
        self.pid = pid
        self.programLength = length
        self.programName = programname
    
    def incrementPc(self):
        #Increment program counter in order to goes to the next instruction of the program
        self.pc += 1


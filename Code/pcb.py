class Pcb:

    def __init__(self, position, pid, count):
        self.pc = 0
        self.pid = pid
        self.memoryPosition = position
        self.programLength = count
    
    def incrementPc(self):
        self.pc += 1


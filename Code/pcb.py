class Pcb:

    def __init__(self, position, count):
        self.pc = 0
        self.pid = 1
        self.memoryPosition = position
        self.programLength = count
    
    def incrementPc(self):
        self.pc += 1



class Kernel:
    def __init__(self):
        pass

    def initializeKernel(self, clock, programLoader, scheduler):
        self.programLoader= programLoader
        self.scheduler= scheduler
        self.clock= clock

    def loadProgram(self, program):
        self.programLoader.load(program)

    def run(self):
        self.scheduler.setNextPcbToCpu()
        self.clock.start()

from threading import Thread


class Kernel(Thread):
    def __init__(self):
        Thread.__init__(self)
        pass

    def initializeKernel(self, clock, programloader, scheduler):
        self.programLoader = programloader
        self.scheduler = scheduler
        self.clock = clock
        self.clock.start()

    def load(self, program):
        self.programLoader.load(program)

    def run(self):
        Thread.run(self)
        self.scheduler.setNextPcbToCpu()

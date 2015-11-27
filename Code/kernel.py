from threading import Thread


class Kernel(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.program = None
        self.isFirstLoad= True

    def initializeKernel(self, clock, programloader, scheduler):
        self.programLoader = programloader
        self.scheduler = scheduler
        self.clock = clock

    def load(self, program):
        #Sets a program that the program loader will load to the memory
        self.program= program

    def run(self):
        Thread.run(self)

        while True:
            if (not self.program == None):

                self.isFirstLoad= len(self.programLoader.pcbTable.pcbs) == 0
                self.programLoader.load(self.program)
                if(self.isFirstLoad):
                    self.scheduler.setNextPcbToCpu()
                self.program= None

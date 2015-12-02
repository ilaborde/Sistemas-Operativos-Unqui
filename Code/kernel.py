import time
from queue import Queue
from threading import Thread


class Kernel(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.programsQueue = Queue()
        self.isFirstLoad = True

    def initializeKernel(self, clock, programloader, scheduler):
        self.programLoader = programloader
        self.scheduler = scheduler
        self.clock = clock

    def load(self, program):
        # Sets a program that the program loader will load to the memory
        self.programsQueue.put_nowait(program)

    def run(self):
        Thread.run(self)

        while True:
            if not self.programsQueue.qsize() == 0:
                program = self.programsQueue.get_nowait()
                self.isFirstLoad = len(self.programLoader.pcbTable.pcbs) == 0
                self.programLoader.load(program)
                if self.isFirstLoad:
                    self.scheduler.setNextPcbToCpu()
                time.sleep(0.1)

from queue import Queue

class Scheduler:
    def __init__(self, cpu):
        self.currentCpu = cpu
        self.currentReadyQueue = Queue()

    def setReadyQueue(self, readyQueue):
        self.currentReadyQueue = readyQueue

    def setNextPcbToCpu(self):
        self.currentCpu.setPcb(self.currentReadyQueue.get())

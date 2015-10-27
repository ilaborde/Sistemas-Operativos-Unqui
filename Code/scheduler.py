from queue import Queue


class Scheduler:
    def __init__(self, cpu,queue):
        self.currentCpu = cpu
        self.currentReadyQueue = queue

    def addPcbToReadyQueue(self, pcb):
        self.currentReadyQueue.put(pcb)

    def setNextPcbToCpu(self):
        self.currentCpu.setPcb(self.currentReadyQueue.get())


class Scheduler:
    def __init__(self, cpu,queue):
        self.currentCpu = cpu
        self.currentReadyQueue = queue

    def addPcbToReadyQueue(self, pcb):
        self.currentReadyQueue.put(pcb)

    def setNextPcbToCpu(self):
        if self.currentReadyQueue.qsize() > 0:
            self.currentCpu.setPcb(self.currentReadyQueue.get())

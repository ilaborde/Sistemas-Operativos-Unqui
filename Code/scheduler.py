class Policies:
    RoundRobin = 1
    Fifo = 2


class Scheduler:
    def __init__(self, cpu, queue, quantum):
        self.currentCpu = cpu
        self.currentReadyQueue = queue
        self.quantum = quantum


    def addPcbToReadyQueue(self, pcb):
        self.currentReadyQueue.put(pcb)

    def setNextPcbToCpu(self):
        if self.currentReadyQueue.qsize() > 0:
            self.currentCpu.setPcb(self.currentReadyQueue.get(), self.quantum)

class Policies:
    RoundRobin = 1
    Fifo = 2


class Scheduler:
    def __init__(self, cpu, queue, quantum, lockReadyQueue):
        self.currentCpu = cpu
        self.currentReadyQueue = queue
        self.quantum = quantum
        self.lockReadyQueue= lockReadyQueue

    def addPcbToReadyQueue(self, pcb):
        self.lockReadyQueue.acquire()
        self.currentReadyQueue.put_nowait(pcb)
        self.lockReadyQueue.release()


    def setNextPcbToCpu(self):
        self.lockReadyQueue.acquire()
        if self.currentReadyQueue.qsize() > 0:
            self.currentCpu.setPcb(self.currentReadyQueue.get_nowait(), self.quantum)
        self.lockReadyQueue.release()


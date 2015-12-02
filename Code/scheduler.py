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
        #Add a pcb into the ready queue for cpu processing
        self.lockReadyQueue.acquire()
        self.currentReadyQueue.put(pcb)
        self.lockReadyQueue.release()


    def setNextPcbToCpu(self):
        #Sets the next pcb to the cpu if the readyQueue isn`t empty
        self.lockReadyQueue.acquire()
        if self.currentReadyQueue.qsize() > 0:

            self.currentCpu.setPcb(self.currentReadyQueue.get(), self.quantum)
        self.lockReadyQueue.release()


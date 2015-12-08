class Policies:
    RoundRobin = 1
    Fifo = 2


class Scheduler:
    def __init__(self, queue, quantum, lockReadyQueue):
        self.currentCpuList = []
        self.currentReadyQueue = queue
        self.quantum = quantum
        self.lockReadyQueue= lockReadyQueue

    def addPcbToReadyQueue(self, pcb):
        #Add a pcb into the ready queue for cpu processing
        self.lockReadyQueue.acquire()
        self.currentReadyQueue.put(pcb)
        self.lockReadyQueue.release()

    def registryCpu(self, cpu):
        self.currentCpuList.append(cpu)

    def setNextPcbToCpu(self):
        #Sets the next pcb to the cpu if the readyQueue isn`t empty
            for cpu in self.currentCpuList:
                self.lockReadyQueue.acquire()
                if self.currentReadyQueue.qsize() > 0 and cpu.currentPcb == None:
                    cpu.setPcb(self.currentReadyQueue.get(), self.quantum)
                self.lockReadyQueue.release()


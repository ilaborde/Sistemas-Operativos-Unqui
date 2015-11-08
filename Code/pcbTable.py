class PcbTable:
    def __init__(self):
        self.pcbs = {}
        self.pids = 0

    def addpcb(self, pcb):
        if pcb.pid in self.pcbs:
            raise ValueError("Critical error: Handle not found")
        else:
            self.pcbs[pcb.pid] = pcb

    def getnewpid(self):
        return self.pids + 1

    def removepcb(self, pid):
        self.pcbs[pid] = None

class PcbTable:
    def __init__(self):
        self.pcbs = {}
        self.pids = 0

    def addpcb(self, pcb):
        if pcb.pid in self.pcbs:
            raise ValueError("There is a pid with the same number")
        else:
            self.pcbs[pcb.pid] = pcb

    def getnewpid(self):
        self.pids += 1
        return  self.pids

    def removepcb(self, pid):
        self.pcbs[pid] = None

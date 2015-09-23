class Clock:
    def __init__(self, cpuToTick):
        self.cpu = cpuToTick

    def tick(self):
        self.cpu.fetch()

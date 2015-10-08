class Clock:
    def __init__(self):
        self.cpuList = []

    def registrycpu(self, cpu):
        self.cpuList.append(cpu)

    def tick(self):
        for cpu in self.cpuList:
            cpu.fetch()

from threading import Thread
import time


class Clock(Thread):
    def __init__(self):
        self.cpuList = []
        Thread.__init__(self)

    def registrycpu(self, cpu):
        self.cpuList.append(cpu)

    def run(self):
        while True:
            time.sleep(1)
            self.tick()

    def tick(self):
        for cpu in self.cpuList:
            cpu.fetch()

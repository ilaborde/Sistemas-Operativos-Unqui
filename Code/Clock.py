from threading import Thread
import time


class Clock(Thread):
    def __init__(self):
        self.cpuList = []
        Thread.__init__(self)

    def registrycpu(self, cpu):
        self.cpuList.append(cpu)

    def run(self):
        print('initializing clock')
        for cpu in self.cpuList:
            cpu.start()
        while True:
            self.tick()
            time.sleep(1)

    def tick(self):
        for cpu in self.cpuList:
            cpu.fetch()

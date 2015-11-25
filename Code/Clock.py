from threading import Thread
import time


class Clock(Thread):
    def __init__(self,lockProcessing):
        self.cpuList = []
        Thread.__init__(self)
        self.lockProcessing= lockProcessing

    def registrycpu(self, cpu):
        self.cpuList.append(cpu)

    def run(self):
        print('initializing clock')
        for cpu in self.cpuList:
           cpu.daemon= True
           cpu.start()

        while True:
            self.lockProcessing.acquire()
            self.tick()
            self.lockProcessing.release()
            time.sleep(0.5)

    def tick(self):
        for cpu in self.cpuList:
            cpu.fetch()

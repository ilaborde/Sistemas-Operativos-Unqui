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
        while True:
            self.lockProcessing.acquire()
            if (self.tick()):
                self.lockProcessing.wait()
            self.lockProcessing.release()
            time.sleep(0.5)

    def tick(self):
        clockShouldWait= False
        for cpu in self.cpuList:
            shouldWait= cpu.fetch()
            clockShouldWait= clockShouldWait or shouldWait
        return clockShouldWait

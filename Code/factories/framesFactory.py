from queue import Queue

from Code.memoryFrame import MemoryFrame


class FramesFactory:
    def __init__(self):
        self.freeMemoryFrames = Queue()

    def createElement(self, memorylen):
        for i in range(0, int((memorylen / 4))):
            self.freeMemoryFrames.put(MemoryFrame(i + 1, 4, i * 4))
        return self.freeMemoryFrames

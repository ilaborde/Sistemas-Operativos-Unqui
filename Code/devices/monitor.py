from queue import Queue

class Monitor:

    def __init__(self):
       self.queue = Queue()

    def pushToQueue(self,instruction,pcb):
        self.queue.put(pcb)
        print(instruction.text)

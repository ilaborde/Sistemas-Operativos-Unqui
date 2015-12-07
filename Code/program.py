from queue import Queue


class Program:
    def __init__(self):
        self.instructions = []
        self.queueInstructions = Queue()
    def add(self, instruction):
        #Add instructions into the program
        self.instructions.append(instruction)

    def refreshInstructions(self):
        for i in range(0,len(self.instructions)):
            self.queueInstructions.put(self.instructions[i])


            
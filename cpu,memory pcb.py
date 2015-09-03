##
##class InterruptionHandle:
##
##    def handle(self, irq):
##        ....
##
##    def finishProgramInterruption(self):
##        print ("Finished...")
##


class Memory:

    def __init__(self):
        self.cells = []

    def put(self, programInstructions):
        self.cells= self.cells + programInstructions
        return len(self.cells) - len(programInstructions)
        
    def get(self, index):
        return self.cells[index]
        
        
class Pcb:

      def __init__(self, position, count):
          self.pc= 0
          self.PcbId = 1
          self.memoryPosition= position
          self.programCount= count

      def IncrementPc(self):
          self.pc= self.pc + 1
          
        
class Cpu:

    def __init__(self, memo, handle):
       
          self.memory= memo
          self.interruptionHandle= handle
    def setPcb(self, pcb):
        self.currentPcb = pcb
        
    def fetch(self):
        print (self.memory.get(self.currentPcb.pc + self.currentPcb.memoryPosition))
        self.currentPcb.IncrementPc()

        if (self.currentPcb.pc == self.currentPcb.programCount):
            self.interruptionHandle.finishProgramInterruption()

class InterruptionHandle:
    
    def finishProgramInterruption(self):
        print ("Finished...")
        


program= [1,2,3]
program2= [4,5,6]
memory= Memory()
cpu= Cpu(memory, InterruptionHandle())
initialPosition = memory.put(program)
initialPosition2= memory.put(program2)

pcb= Pcb(initialPosition, len(program))
pcb2= Pcb(initialPosition2, len(program2))

cpu.setPcb(pcb)
cpu.fetch()
cpu.fetch()
cpu.fetch()

print ("--------------------")

cpu.setPcb(pcb2)
cpu.fetch()
cpu.fetch()
cpu.fetch()





        
        
        
        
          

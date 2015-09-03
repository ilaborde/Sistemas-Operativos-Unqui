import unittest

class Program:
    
    def __init__(self):
        self.instructions = []
              
    def add(self,lala):
        self.instructions.append(lala)

    def run(self):
        for x in self.instructions:
            x.imprimir()
    def instructionsSize(self):
        return len(self.instructions)
    

class Instruction:

    def __init__(self,text):
        self.text = text
        
    def imprimir(self):
        print (self.text)


class TestStringMethods(unittest.TestCase):

  def setUp(self):
      self.program= Program()

  def test_addInstruction(self):
      
     self.program.add(Instruction("re"))
     self.assertEqual(self.program.instructionsSize(), 1)

  

      
     


    




  
    
                           
       

    

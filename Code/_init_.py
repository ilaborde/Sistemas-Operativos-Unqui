from Code.Console import Console
from Code.factories.kernelFactory import *
from Code.shell import Shell

if __name__ == '__main__':

    #  Names of the programs loaded: program0, program1 or program2, to run a program enter : exec programExample

    c= Shell() #to run cmd console
    c.initializeConsole()


    #----------

    #To run programs without console
    # kernel = kernelFactory().configurationTwo()
    # console = Console()
    # kernel.load("program0")
    # kernel.load("program0")
    # kernel.load("program0")
    # kernel.load("program0")

    #----------
    # kernel = kernelFactory().configurationTwo()
    # console = Console()
    # console.start(kernel) #to run simple console
    # console.run()









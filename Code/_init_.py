from Code.factories.kernelFactory import *

if __name__ == '__main__':
    kernel = kernelFactory().selectConfiguration(1)
    kernel.loadProgram("program0")
    kernel.run()

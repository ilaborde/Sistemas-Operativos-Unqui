from Code.factories.kernelFactory import *

if __name__ == '__main__':
    kernel = kernelFactory().selectConfiguration(1)
    kernel.load("program0")
    kernel.load("program1")
    kernel.start()
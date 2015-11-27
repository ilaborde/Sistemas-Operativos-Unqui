import time
from Code.factories.kernelFactory import *

def console():

    x= ""

    while True:

        print ("Enter program...")
        x=  input("program: " )
        kernel.load(x)


if __name__ == '__main__':

    kernel = kernelFactory().selectConfiguration(1)
    #mock shell
    console()


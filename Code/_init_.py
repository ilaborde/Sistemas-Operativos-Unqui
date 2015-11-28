from Code.factories.kernelFactory import *


def console():
    x = ""
    kernel.load("program0")
    kernel.load("program1")
    while True:
        print("Enter program...")
        x = input("program: ")


if __name__ == '__main__':
    kernel = kernelFactory().selectConfiguration(1)
    # mock shell
    console()

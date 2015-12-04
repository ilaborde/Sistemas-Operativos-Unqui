import platform

import sys

from subprocess import Popen

from Code.Console import Console
from Code.factories.kernelFactory import *

if __name__ == '__main__':
    kernel = kernelFactory().selectConfiguration(1)
    console = Console()
    # mock shell
    # Names of the programs loaded: program0, program1 or program2, to run a program enter : exec programExample
    console.start(kernel)
    console.run()


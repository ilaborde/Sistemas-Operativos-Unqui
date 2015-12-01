from Code.Console import Console
from Code.factories.kernelFactory import *

if __name__ == '__main__':
    kernel = kernelFactory().selectConfiguration(1)
    console = Console()
    # mock shell
    console.start(kernel)

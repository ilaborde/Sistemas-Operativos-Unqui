import platform

import sys

from subprocess import Popen

from Code.Console import Console
from Code.factories.kernelFactory import *

if __name__ == '__main__':
    kernel = kernelFactory().selectConfiguration(1)
    console = Console()
    # mock shell
    console.start(kernel)
    console.run()

    # messages = 'This is Console1', 'This is Console2'
    #
    # if platform.system() == "Windows":
    #       new_window_command = "cmd.exe /c start".split()
    # else:  #XXX this can be made more portable
    #       new_window_command = "x-terminal-emulator -e".split()
    #
    #     # open new consoles, display messages
    # echo = [sys.executable, "-c",
    #             "from Code.factories.kernelFactory import * ;"
    #             "from Code.Console import Console  ;"
    #             "kernel = kernelFactory().selectConfiguration(1) ;"
    #             "console = Console() ;"
    #             "console.start(kernel) ;"
    #             "console.run() ;"]
    #
    # processes = [Popen(new_window_command + echo + [msg]) for msg in messages]
    #
    # # wait for the windows to be closed
    # #for proc in processes:
    # processes[0].wait()
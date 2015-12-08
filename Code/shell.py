import os
import sys
import platform
from subprocess import Popen
from threading import Thread


import threading
from tkinter import Frame, END, Text, Tk
from Tools.Scripts.treesync import raw_input


class Shell(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.window= ""
        self.title= "Cmd"
        self.echo= ""
        self.process= None
        self.x= ""

    def printText(self, line):

        pass



    def initializeConsole(self):


        # define a command that starts new terminal
        if platform.system() == "Windows":
            self.window= "cmd.exe /c start".split()
        else:  #XXX this can be made more portable
            self.window = "x-terminal-emulator -e".split()
        self.x= "d"
        # open new consoles, display messages
        echo = [sys.executable, "-c",
                "from Code.Console import Console ; "
                "from Code.factories.kernelFactory import * ;"
                "kernel = kernelFactory().selectConfiguration(1) ;"
                "console = Console(); "
                "console.start(kernel) ;"
                "console.run();"]
        self.process = Popen(self.window + echo + [self.title])

        # wait for the windows to be closed





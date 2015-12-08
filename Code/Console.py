from threading import Thread
import sys
from tkinter import Tk, Label, mainloop


class Console(Thread):

    def __init__(self):
        commandList = ['1','2','4','5']
        Thread.__init__(self)
        self.kernel= None

    def start(self, kernel):
        self.kernel= kernel

    def run(self):
        Thread.run(self)

        while True:

              command = input('> Enter a command: ').strip().lower()
              com = command.split()
              if com[0] == 'exec':
                 self.kernel.load(com[1])

              elif com[0] == 'list':
                print('Doing something else')
              elif com[0] == 'quit':
                print('shutting down...')
                self.kernel.shouldShutDown= True
                raise SystemExit
              else:
                print('Invalid Command.')








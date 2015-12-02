from tkinter import font, Text, Tk, INSERT, END
from Tools.scripts.treesync import raw_input
from threading import Thread


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

              command = raw_input('Enter a command: ').strip().lower()
              com = command.split()
              if com[0] == 'exec':
                 self.kernel.load(com[1])
              elif com[0] == 'list':
                print('Doing something else')
              elif com[0] == 'quit':
                print('shutting down...')
                quit()
              else:
                print('Invalid Command.')








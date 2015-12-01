from Tools.Scripts.treesync import raw_input


class Console:

    def __init__(self):
        commandList = ['1','2','4','5']

    def start(self,kernel):
        while True:
            # print("Enter a command")
            # x = input("program: ")
            # kernel.load(x)
            command = raw_input('Enter a command: ').strip().lower()
            com = command.split()
            if com[0] == 'exec':
                kernel.load(com[1])
            elif com[0] == 'list':
                print('Doing something else')
            elif com[0] == 'quit':
                print('shutting down...')
                quit()
            else:
                print('Invalid Command.')


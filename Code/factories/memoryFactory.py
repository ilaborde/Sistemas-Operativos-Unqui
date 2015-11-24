from Code.memory import Memory

class MemoryFactory:

    def __init__(self):
        pass

    def createElement(self, lock):
        return Memory(lock)



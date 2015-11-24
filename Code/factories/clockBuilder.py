from Code.Clock import Clock


class ClockBuilder:

    def __init__(self):
        pass

    def createElement(self, cpu):

        clock = Clock()
        clock.registrycpu(cpu)

        return clock



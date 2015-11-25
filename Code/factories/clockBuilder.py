from Code.Clock import Clock


class ClockBuilder:

    def __init__(self):
        pass

    def createElement(self, cpu, lockProcessing):

        clock = Clock(lockProcessing)
        clock.registrycpu(cpu)

        return clock



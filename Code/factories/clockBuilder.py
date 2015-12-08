from Code.Clock import Clock


class ClockBuilder:

    def __init__(self):
        pass

    def createElement(self, lockProcessing):

        clock = Clock(lockProcessing)
        return clock



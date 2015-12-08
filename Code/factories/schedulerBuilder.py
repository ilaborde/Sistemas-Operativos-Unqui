from Code.scheduler import Scheduler


class SchedulerBuilder:

    def __init__(self):
        pass

    def createElement(self, queue, quantum, lock):
        return Scheduler(queue, quantum, lock)
from Code.scheduler import Scheduler


class SchedulerFactory:

    def __init__(self):
        pass

    def createElement(self, cpu, queue):

        return Scheduler(cpu,queue, 3)
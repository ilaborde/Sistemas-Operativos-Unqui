from Code.scheduler import Scheduler


class SchedulerFactory:

    def __init__(self):
        pass

    def createElement(self, cpu, queue, quantum):

        return Scheduler(cpu,queue, quantum)
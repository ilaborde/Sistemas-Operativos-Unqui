from Code.scheduler import Scheduler


class SchedulerBuilder:

    def __init__(self):
        pass

    def createElement(self, cpu, queue, quantum, lock):
        return Scheduler(cpu,queue, quantum, lock)
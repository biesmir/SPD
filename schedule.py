from random import randint
from job import Job

class Schedule:
    """Klasa przechowująca informacje o kolejności wykonywania zadań"""

    def __init__(self, joblist, number_of_jobs, number_of_machines, name = "bez nazwy"):
        self.name = name
        self.joblist = joblist
        self.number_of_jobs = number_of_jobs
        self.number_of_machines = number_of_machines

    def cmax(self):
        return self.cpi(self.number_of_jobs - 1, self.number_of_machines -1)

    def cpi(self, job, machine):
        if machine == -1:
            return 0

        if job == -1:
            return 0

        else:
            return max(self.cpi(job - 1, machine), self.cpi(job, machine - 1)) + self.joblist[job].time[machine]

    def make_random(self, machines, jobs):
        for i in range(jobs):
            self.joblist.append(Job([randint(1, 9) for j in range(machines)]))


from random import randint
from job import Job


class Schedule:
    """Klasa przechowująca informacje o kolejności wykonywania zadań"""

    def __init__(self, joblist=[], name="bez nazwy"):
        self.name = name
        self.joblist = joblist
        self.number_of_jobs = len(joblist)
        if self.number_of_jobs != 0:
            self.number_of_machines = len(joblist[0].time)
        else:
            self.number_of_machines = 0

    def cmax(self):
        self.number_of_jobs = len(self.joblist)
        self.number_of_machines = len(self.joblist[0].time)
        return int(self.cpi(self.number_of_jobs - 1, self.number_of_machines - 1))

    def cpi(self, job, machine):
        if machine == -1:
            return 0

        if job == -1:
            return 0

        else:
            return max(self.cpi(job - 1, machine), self.cpi(job, machine - 1)) + self.joblist[job].time[machine]

    def make_random(self, jobs, machines):
        for i in range(jobs):
            self.joblist.append(Job([randint(1, 9) for j in range(machines)], index=i, name=("zadanie " + str(i+1))))
        self.number_of_jobs = jobs
        self.number_of_machines = machines

    def __str__(self):
        string = ""
        for i in self.joblist:
            string += i.__str__() + "\n"
        return string

    def johnson(self):
        if self.number_of_machines == 2:
            self.joblist.sort()
            sequence1 = []
            sequence2 = []

            for i in range(self.number_of_jobs):
                if self.joblist[i].time[0] <= self.joblist[i].time[1]:
                    sequence1.append(self.joblist[i])
                else:
                    sequence2.append(self.joblist[i])
            sequence = sequence1 + list(reversed(sequence2))
            self.joblist = sequence

        elif self.number_of_machines == 3:
            virtual_machines_list = []
            for job in self.joblist:
                virtual_machines_list.append(Job([job.time[0] + job.time[1], job.time[1] + job.time[2]], index=job.index))

            virtual_machines_list.sort()

            sequence1 = []
            sequence2 = []
            for job in virtual_machines_list:
                if job.time[0] <= job.time[1]:
                    sequence1.append(self.joblist[job.index])
                else:
                    sequence2.append(self.joblist[job.index])

            self.joblist = sequence1 + list(reversed(sequence2))

        else:
            print("brak algorytmu dla tej liczby maszyn")
            return

    def load_from_file(self, file_name):
        with open(file_name) as file:
            line = file.readline()
            line = list(map(int, line.split()))
            self.number_of_jobs = line[0]
            self.number_of_machines = line[1]

            for i, line in enumerate(file.readlines()):
                self.joblist.append(Job(list(map(int, line.split())), index=i, name="zadanie " + str(i + 1)))
                # print(list(map(int, line.split())))

    def basic_neh(self):
        """Podstawowy algorytm NEH"""
        best = {"minimum time": 0,
                "best_position": 0}
        self.joblist.sort(reverse=True, key=lambda x: x.cmax)
        tmp_schedule = Schedule([])

        for i in range(self.number_of_jobs):
            tmp_schedule.joblist.insert(0, self.joblist[i])
            best["minimum time"] = tmp_schedule.cmax()
            best["best_position"] = 0
            del tmp_schedule.joblist[0]

            for j in range(i+1):

                tmp_schedule.joblist.insert(j, self.joblist[i])
                if best["minimum time"] >= tmp_schedule.cmax():
                    best["minimum time"] = tmp_schedule.cmax()
                    best["best_position"] = j
                del tmp_schedule.joblist[j]

            tmp_schedule.joblist.insert(best["best_position"], self.joblist[i])

        self.joblist = tmp_schedule.joblist

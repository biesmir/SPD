from random import randint
from job import Job


class Schedule:
    """Klasa przechowująca informacje o kolejności wykonywania zadań"""

    def __init__(self, joblist=[], name="bez nazwy"):
        self.name = name
        self.joblist = joblist
        self.number_of_jobs = len(joblist)
        self.mtime = 0
        self.partial_cmax = []
        if self.number_of_jobs != 0:
            self.number_of_machines = len(joblist[0].time)
        else:
            self.number_of_machines = 0

    def opt_cmax(self):

        self.number_of_jobs = len(self.joblist)
        self.number_of_machines = len(self.joblist[0].time)
        self.partial_cmax = [[0 for x in range(self.number_of_machines+1)] for y in range(self.number_of_jobs+1)]
        return int(self.opt_cpi(self.number_of_jobs - 1, self.number_of_machines - 1))

    def opt_cpi(self, job, machine):
        if machine == -1:
            return 0

        if job == -1:
            return 0

        if self.partial_cmax[self.number_of_jobs][self.number_of_machines] != 0:
            return self.partial_cmax[self.number_of_jobs][self.number_of_machines]

        else:
            self.partial_cmax[self.number_of_jobs][self.number_of_machines] = max(self.cpi(job - 1, machine), self.cpi(job, machine - 1)) + self.joblist[job].time[machine]
            return self.partial_cmax[self.number_of_jobs][self.number_of_machines]

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

    def ncmax(self):
        #zapisujemy czas zakończenia zadania 1 na kolejnych maszynach
        self.joblist[0].end_time[0] = self.joblist[0].time[0]
        for i in range(1, self.number_of_machines):
            self.joblist[0].end_time[i] = self.joblist[0].time[i] + self.joblist[0].end_time[i - 1]

        #zapisujemy czas zakończenia zadań na 1 maszynie
        for i in range(1, self.number_of_jobs):
            self.joblist[i].end_time[0] = self.joblist[i].time[0] + self.joblist[i-1].end_time[0]

        for i in range(1, self.number_of_machines):
            for j in range(1, self.number_of_jobs):
                self.joblist[j].end_time[i] = max(self.joblist[j].end_time[i-1], self.joblist[j-1].end_time[i]) \
                                              + self.joblist[j].time[i]

        return self.joblist[self.number_of_jobs - 1].end_time[self.number_of_machines - 1]

    def make_random(self, jobs, machines):
        self.joblist = []
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
        self.joblist = []
        with open(file_name) as file:
            line = file.readline()
            line = file.readline()
            while "data" not in line:
                pass
                line = file.readline()
            line = file.readline()
            line = list(map(int, line.split()))
            self.number_of_jobs = line[0]
            self.number_of_machines = line[1]

            for i, line in enumerate(file.readlines()):
                if line != '\n':
                    self.joblist.append(Job(list(map(int, line.split())), index=i, name="zadanie " + str(i + 1)))

    def basic_neh(self):
        """Podstawowy algorytm NEH"""

        best = {"minimum time": 0,
                "best_position": 0}
        self.joblist.sort(reverse=True, key=lambda x: x.omega)
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

    def opt_neh(self):
        """Algorytm neh wykorzystujący mniej obliczeń dla cmax"""

        best = {"minimum time": 0,
                "best_position": 0}
        self.joblist.sort(reverse=True, key=lambda x: x.omega)
        tmp_schedule = Schedule([])

        for i in range(self.number_of_jobs):
            tmp_schedule.joblist.insert(0, self.joblist[i])
            best["minimum time"] = tmp_schedule.opt_cmax()
            best["best_position"] = 0
            del tmp_schedule.joblist[0]

            for j in range(i+1):

                tmp_schedule.joblist.insert(j, self.joblist[i])
                if best["minimum time"] >= tmp_schedule.opt_cmax():
                    best["minimum time"] = tmp_schedule.opt_cmax()
                    best["best_position"] = j
                del tmp_schedule.joblist[j]

            tmp_schedule.joblist.insert(best["best_position"], self.joblist[i])

        self.joblist = tmp_schedule.joblist

    def a_neh(self):
        """Algorytm NEH z akceleracja"""

        best = {"minimum time": 0,
                "best_position": 0}
        self.joblist.sort(reverse=True, key=lambda x: x.omega)
        tmp_schedule = Schedule([])
        prev_cmax = 0
        prev_joblist = []

        for i in range(self.number_of_jobs):
            tmp_schedule.joblist.insert(0, self.joblist[i])
            best["minimum time"] = tmp_schedule.cmax()
            best["best_position"] = 0
            del tmp_schedule.joblist[0]

            for j in range(i+1):
                tmp_schedule.joblist.insert(j, self.joblist[i])
                if i == self.number_of_jobs:
                    for k in range(self.number_of_jobs):
                        while prev_joblist[k] == tmp_schedule.joblist[k]:
                            add_schedule = tmp_schedule
                        for x in range(k-1):
                            del add_schedule.joblist[x]
                        act_cmax = prev_cmax + add_schedule.cmax()
                        if prev_joblist[k] != tmp_schedule.joblist[k]:
                          act_cmax = tmp_schedule.cmax()
                else:
                    act_cmax = tmp_schedule.cmax()

                if best["minimum time"] >= act_cmax:
                    best["minimum time"] = act_cmax
                    best["best_position"] = j
                prev_cmax = act_cmax
                prev_joblist = tmp_schedule.joblist
                del tmp_schedule.joblist[j]


            tmp_schedule.joblist.insert(best["best_position"], self.joblist[i])
        self.joblist = tmp_schedule.joblist

    def extend_neh_lng(self):
        """Podstawowy algorytm NEH"""

        best = {"minimum time": 0,
                "best_position": 0}
        self.joblist.sort(reverse=True, key=lambda x: x.omega)
        tmp_schedule = Schedule([])

        for i in range(self.number_of_jobs):
            tmp_schedule.joblist.insert(0, self.joblist[i])
            best["minimum time"] = tmp_schedule.cmax()
            best["best_position"] = 0
            del tmp_schedule.joblist[0]

            for j in range(i+1):

                tmp_schedule.joblist.insert(j, self.joblist[i])
                if best["minimum time"] > tmp_schedule.cmax():
                    best["minimum time"] = tmp_schedule.cmax()
                    best["best_position"] = j
                del tmp_schedule.joblist[j]

            tmp_schedule.joblist.insert(best["best_position"], self.joblist[i])

            #best["minimum time"] = tmp_schedule.cmax()
            #best["best_position"] = 0
            job = max(tmp_schedule.joblist, key=lambda x: x.omega)
            tmp_schedule.joblist.remove(job)

            for j in range(i+1):

                tmp_schedule.joblist.insert(j, job)
                if best["minimum time"] > tmp_schedule.cmax():
                    best["minimum time"] = tmp_schedule.cmax()
                    best["best_position"] = j
                del tmp_schedule.joblist[j]

            tmp_schedule.joblist.insert(best["best_position"], self.joblist[i])

        self.joblist = tmp_schedule.joblist

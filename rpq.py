class Job:
    def __init__(self, r: int, p: int, q: int, index=-1):
        self.r = r
        self.p = p
        self.q = q
        self.p_end_time = 0
        self.index = index

    def __str__(self):
        return "job" + str(self.index) + '\n'

    def __repr__(self):
        return "job" + str(self.index) + '\n'


class Schedule:
    def __init__(self, file_name="", job_list=[]):
        if file_name == "":
            self.job_list = job_list
            self.number_of_jobs = len(job_list)
        else:
            self.job_list = []
            self.load_from_file(file_name)

    def __copy__(self):
        return Schedule(job_list=self.job_list)

    def cmax(self):
        self.job_list[0].p_end_time = self.job_list[0].r + self.job_list[0].p
        for i in range(1, len(self.job_list)):
            self.job_list[i].p_end_time = max(self.job_list[i-1].p_end_time, self.job_list[i].r) +\
                                          self.job_list[i].p

        last = max(self.job_list, key=lambda x: x.q + x.p_end_time)
        return last.p_end_time + last.q

    def load_from_file(self, file_name):
        with open(file_name) as file:
            line = file.readline()
            line = list(map(int, line.split()))
            self.number_of_jobs = line[0]
            for i, line in enumerate(file.readlines()):
                if line != '\n':
                    rpq_times = list(map(int, line.split()))
                    self.job_list.append(Job(r=rpq_times[0], p=rpq_times[1], q=rpq_times[2], index=i))
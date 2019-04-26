class Job:
    def __init__(self, r: int, p: int, q: int):
        self.r = r
        self.p = p
        self.q = q
        self.p_end_time = 0


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
        for i in range(1, self.number_of_jobs):
            self.job_list[i].p_end_time = max(self.job_list[i-1].p_end_time, self.job_list[i].r) +\
                                          self.job_list[i].p

        return self.job_list[-1].p_end_time + self.job_list[-1].q

    def load_from_file(self, file_name):
        with open(file_name) as file:
            line = file.readline()
            line = list(map(int, line.split()))
            self.number_of_jobs = line[0]
            for line in file.readlines():
                if line != '\n':
                    rpq_times = list(map(int, line.split()))
                    self.job_list.append(Job(rpq_times[0], rpq_times[1], rpq_times[2]))




from random import randint
from heap import HeapQ, HeapR
import sys


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

    def __copy__(self):
        return Job(self.r, self.p, self.q, self.index)


class Schedule:
    def __init__(self, file_name="", job_list=[], randomize=False, length=0):
        if file_name == "":
            self.job_list = job_list
            self.number_of_jobs = len(job_list)
        else:
            self.job_list = []
            self.load_from_file(file_name)
        if randomize:
            for i in range(length):
                self.job_list.append(Job(randint(1, 100), randint(1, 40), randint(1, 100), index=i))
            self.number_of_jobs = len(job_list)

    def __copy__(self):
        return Schedule(job_list=[job.__copy__() for job in self.job_list])

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


def schrage(schdl):
    sig = []
    nn = schdl
    ng = Schedule(job_list=[])
    t = min(nn.job_list, key=lambda x: x.r).r
    # print(t)

    while ng.job_list != [] or nn.job_list != []:
        while nn.job_list != [] and min(nn.job_list, key=lambda x: x.r).r <= t:

            j = min(nn.job_list, key=lambda x: x.r)
            ng.job_list.append(j)
            nn.job_list.remove(j)

        if not ng.job_list:
            t = min(nn.job_list, key=lambda x: x.r).r
        else:
            j = max(ng.job_list, key=lambda x: x.q)

            ng.job_list.remove(j)
            sig.append(j)
            t += j.p
    return Schedule(job_list=sig)


def schrage_pmtn(schdl):
    Cmax = 0
    nn = schdl
    ng = Schedule(job_list=[])
    t = 0
    l = 0

    while ng.job_list != [] or nn.job_list != []:
        while nn.job_list != [] and min(nn.job_list, key=lambda x: x.r).r <= t:

            j = min(nn.job_list, key=lambda x: x.r)
            ng.job_list.append(j)
            nn.job_list.remove(j)

            if l != 0:
                if j.q > l.q:
                    l.p = t - j.r
                    t = j.r

                    if l.p > 0:
                        ng.job_list.append(l)

        if not ng.job_list:
            t = min(nn.job_list, key=lambda x: x.r).r
        else:
            j = max(ng.job_list, key=lambda x: x.q)

            ng.job_list.remove(j)
            l = j
            t += j.p
            Cmax = max(Cmax, t+j.q)
    return Cmax


def schrage_heap(schdl):
    sig = []
    nn = HeapR(schdl)
    ng = HeapQ()
    t = nn.array[0].r
    # print(t)

    while ng.array != [] or nn.array != []:
        while nn.array != [] and nn.array[0].r <= t:

            j = nn.pop()
            ng.push(j)

        if not ng.array:
            t = nn.array[0].r
        else:
            j = ng.pop()
            sig.append(j)
            t += j.p
    return Schedule(job_list=sig)


def schrage_pmtn_heap(schdl):
    Cmax = 0
    nn = HeapR(schdl)
    ng = HeapQ()
    t = 0
    l = 0

    while ng.array != [] or nn.array != []:
        while nn.array != [] and nn.array[0].r <= t:

            j = nn.pop()
            ng.push(j)
            if l != 0:
                if j.q > l.q:
                    l.p = t - j.r
                    t = j.r

                    if l.p > 0:
                        ng.push(l)

        if not ng.array:
            t = nn.array[0].r
        else:
            j = ng.pop()
            l = j
            t += j.p
            Cmax = max(Cmax, t + j.q)
    return Cmax


def carlier(schdl, ub=float("inf")):

    pi = schrage_heap(schdl.__copy__())
    u = pi.cmax()
    i = -1

    if u < ub:
        pi_star = pi
        ub = u

    b = -1
    while not (pi.job_list[i].p_end_time + pi.job_list[i].q == pi.cmax()):
        i -= 1
        b = i

    while pi.job_list[i-1].p_end_time == pi.job_list[i].p_end_time - pi.job_list[i].p:
        i -= 1
        a = i
        if i == -len(pi.job_list):
            break
    i = b-1
    c = 0
    while not pi.job_list[b].q > pi.job_list[i].q and i > -len(pi.job_list):
        i -= 1
    if b != i > a:
        c = i
    if not c:
        try:
            return pi_star, ub
        except NameError:
            return pi, ub
    if b != -1:
        k = pi.job_list[c:b + 1]
    else:
        k = pi.job_list[c + 1:]
    rk = min(k, key=lambda x: x.r).r
    qk = min(k, key=lambda x: x.q).q
    pk = sum(elem.p for elem in k)

    rc = pi.job_list[c].r
    rpi = pi.job_list[c].index
    tmp = max(pi.job_list[c].r, rk+pk)
    pi.job_list[c].r = max(pi.job_list[c].r, rk+pk)
    tmp = pi.job_list[c]

    hk = rk + pk + qk
    k_c = pi.job_list[c-1:b+1]

    rk_c = min(k_c, key=lambda x: x.r).r
    qk_c = min(k_c, key=lambda x: x.q).q
    pk_c = sum(elem.p for elem in k_c)
    hk_c = rk_c + qk_c + pk_c

    lb = schrage_pmtn_heap(pi.__copy__())
    lb = max(hk, hk_c, lb)

    if lb < ub:
        pi, ub = carlier(pi, ub)

    for job in pi.job_list:
        if job.index == rpi:
            job.r = rc
            break

    qc = pi.job_list[c].q
    qpi = pi.job_list[c].index
    tmp = max(pi.job_list[c].q, qk + pk)
    pi.job_list[c].q = max(pi.job_list[c].q, qk + pk)

    lb = schrage_pmtn_heap(pi.__copy__())
    lb = max(hk, hk_c, lb)

    if lb < ub:
        pi, ub = carlier(pi, ub)
    for job in pi.job_list:
        if job.index == qpi:
            job.q = qc
            break

    return pi, ub

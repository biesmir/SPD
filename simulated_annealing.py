from schedule import Schedule
from random import randint, random
import math


def swap(schdl, schedule_length):

    index1 = randint(0, schedule_length - 1)
    index2 = randint(0, schedule_length - 1)

    # sprawdzamy czy nie wylosowało się dwa razy to samo
    while index1 == index2:
        index1 = randint(0, schedule_length - 1)
        index2 = randint(0, schedule_length - 1)

    schdl.joblist[index2], schdl.joblist[index1] = schdl.joblist[index1], schdl.joblist[index2]


def random_insert(schdl, schedule_length):
    # funkcja może mieć problemy jeśli dostanie harmoonogram krótszy niż 3 zadania
    job_index = randint(0, schedule_length - 1)
    new_index = randint(0, schedule_length - 2)

    # sprawdzamy czy nie wylosowało się dwa razy to samo
    while job_index == new_index:
        job_index = randint(0, schedule_length - 1)
        new_index = randint(0, schedule_length - 2)

    job = schdl.joblist[job_index]
    del schdl.joblist[job_index]
    schdl.joblist.insert(new_index, job)


def annealing(schdl, u=0.98, temp=100, iterations=10, move="swap", op="normal"):
    schedule_lenght = len(schdl.joblist)
    steps = []
    for i in range(iterations):
        tmp_schdl = schdl.__copy__()

        if move == "insert":
            random_insert(tmp_schdl, schedule_lenght)
        else:
            swap(tmp_schdl, schedule_lenght)

        # Nowe rozwiazanie lepsze od obecnego
        if tmp_schdl.cmax() < schdl.cmax():
            schdl = tmp_schdl

        # Nowe rozwiazanie gorsze od obecnego
        else:
            prob = math.exp((schdl.cmax() - tmp_schdl.cmax())/temp)
            if random() < prob:
                schdl = tmp_schdl

        steps.append(schdl.cmax())
        if op == "alternative":
            temp = temp * (i+1)/iterations
        else:
            temp = u * temp

    return int(schdl.cmax()), steps

def annealing_prob(schdl, u=0.98, temp=100, iterations=10, move="swap", op="normal"):
    schedule_lenght = len(schdl.joblist)
    steps = []
    for i in range(iterations):
        tmp_schdl = schdl.__copy__()

        if move == "insert":
            random_insert(tmp_schdl, schedule_lenght)
        else:
            swap(tmp_schdl, schedule_lenght)
        
        # Odrzucenie prawdopodobienstwa 1 dla nowych lepszych rozwiazan
        prob = math.exp((schdl.cmax() - tmp_schdl.cmax())/temp)
        if random() < prob:
            schdl = tmp_schdl

        steps.append(schdl.cmax())
        if op == "alternative":
            temp = temp * (i+1)/iterations
        else:
            temp = u * temp

    return int(schdl.cmax()), steps

def annealing_cmax(schdl, u=0.98, temp=100, iterations=10, move="swap", op="normal"):
    schedule_lenght = len(schdl.joblist)
    steps = []
    for i in range(iterations):
        tmp_schdl = schdl.__copy__()

        if move == "insert":
            random_insert(tmp_schdl, schedule_lenght)
        else:
            swap(tmp_schdl, schedule_lenght)

        # Nowe rozwiazanie lepsze od obecnego
        if tmp_schdl.cmax() < schdl.cmax():
            schdl = tmp_schdl

        # Nowe rozwiazanie gorsze od obecnego
        elif tmp_schdl.cmax() > schdl.cmax():
            prob = math.exp((schdl.cmax() - tmp_schdl.cmax())/temp)
            if random() < prob:
                schdl = tmp_schdl
                
        else:
            continue
            
        steps.append(schdl.cmax())
        if op == "alternative":
            temp = temp * (i+1)/iterations
        else:
            temp = u * temp

    return int(schdl.cmax()), steps
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


def annealing(schdl, u=0.98, temp=100, iterations=10):
    schedule_lenght = len(schdl.joblist)
    steps = []
    for i in range(iterations):
        tmp_schdl = schdl.__copy__()
        swap(tmp_schdl, schedule_lenght)

        if tmp_schdl.cmax() < schdl.cmax():
            schdl = tmp_schdl
            steps.append(tmp_schdl.cmax())

        else:
            prob = math.exp((schdl.cmax() - tmp_schdl.cmax())/temp)
            if random() < prob:
                schdl = tmp_schdl
                steps.append(tmp_schdl.cmax())

        temp = u * temp

    return steps

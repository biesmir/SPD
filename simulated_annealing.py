from schedule import Schedule
from random import randint, random
import math


def swap(schdl, schedule_length):

    index1 = randint(0, schedule_length - 1)
    index2 = randint(0, schedule_length - 1)

    while index1 == index2:
        index1 = randint(0, schedule_length - 1)
        index2 = randint(0, schedule_length - 1)

    schdl.joblist[index2], schdl.joblist[index1] = schdl.joblist[index1], schdl.joblist[index2]


def annealing(schdl, u=0.98, temp=100, iterations=10):
    schedule_lenght = len(schdl.joblist)

    for i in range(iterations):
        tmp_schdl = schdl.__copy__()
        swap(tmp_schdl, schedule_lenght)

        if tmp_schdl.cmax() < schdl.cmax():
            schdl = tmp_schdl
            print(tmp_schdl.cmax())

        else:
            prob = math.exp((schdl.cmax() - tmp_schdl.cmax())/temp)
            if random() < prob:
                schdl = tmp_schdl
                print(tmp_schdl.cmax())

        temp = u * temp

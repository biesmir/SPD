from schedule import Schedule
from simulated_annealing import *
import matplotlib.pyplot as plt
%matplotlib inline

def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p
        for i in range(low + 1, len(xs)):
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p
            xs[low], xs[i] = xs[i], xs[low]


schdl = Schedule()
#schdl.load_from_file("ta4")
schdl.make_random(9, 5)

u=0.98
temp=100
iterations=100
schedule_lenght = len(schdl.joblist)
steps1 = []
for i in range(iterations):
    tmp_schdl = schdl.__copy__()
    swap(tmp_schdl, schedule_lenght)
    if tmp_schdl.cmax() < schdl.cmax():
        schdl = tmp_schdl
    else:
        prob = math.exp((schdl.cmax() - tmp_schdl.cmax())/temp)
        if random() < prob:
            schdl = tmp_schdl

    steps1.append(schdl.cmax())
    temp = u * temp

cmax = []
for p in permute(schdl.joblist):
    cmax.append(schdl.cmax())

plt.plot(steps1)
plt.show()
plt.plot(cmax)
plt.show()
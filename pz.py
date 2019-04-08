from schedule import Schedule
import pickle


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

max_jobs = 15

for i in range(5, max_jobs):

    cmax = []
    schdl.make_random(i, 5)
    with open("./permutations/inc_"+str(i)+"j5m", 'wb') as pzfile:
        pickle.dump(schdl, pzfile)
    for p in permute(schdl.joblist):
        cmax.append(int(schdl.cmax()))
    with open("./permutations/pz"+str(i)+"j5m", 'wb') as pzfile:
        pickle.dump(cmax, pzfile)
    print("przegląd ok")

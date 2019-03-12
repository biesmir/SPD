from job import Job
from schedule import Schedule

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


# czas1 = [4, 5, 3]
# czas2 = [5, 2, 3]
# czas3 = [1, 6, 3]
#
# zadanie1 = Job(czas1)
# zadanie2 = Job(czas2)
# zadanie3 = Job(czas3)
#
# harmonogram = Schedule([zadanie1, zadanie2, zadanie3], 3, len(czas1))

harmonogram = Schedule([], 3, 3)
harmonogram.make_random(3, 3)

# print(harmonogram)
for i in permute(harmonogram.joblist):
    print(harmonogram.cmax())

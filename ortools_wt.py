from __future__ import print_function
from ortools.linear_solver import pywraplp
from pathlib import Path
from ortools.sat.python import cp_model
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import solver_parameters_pb2


class PWD():
    def __init__(self, p, w, d):
        self.P = p
        self.W = w
        self.D = d


def Milp_WT(jobs, instanceName):
    sumaP = []
    for x in range(len(jobs)):
        sumaP.append(jobs[x].P)
    variableMaxValue = sum(job.W*(sum(sumaP)-job.D) if sum(sumaP)-job.D > 0 else 0 for job in jobs)
    solver = pywraplp.Solver('simple_mip_program',
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    starts = [(solver.IntVar(0, variableMaxValue, "starts"+str(i))) for i in range(len(jobs))]
    penalty = [(solver.IntVar(0, variableMaxValue, "kara"+str(i))) for i in range(len(jobs))]
    suma_wT = solver.IntVar(0, variableMaxValue, "suma_wT")

    for i in range(1, len(jobs)):
        solver.Add(starts[i] >= starts[i-1]+jobs[i-1].P)
        solver.Add(penalty[i] >= (starts[i] + jobs[i].P - jobs[i].D) * jobs[i].W if (starts[i] + jobs[i].P - jobs[i].D) >= 0 else 0)
    solver.Add(suma_wT >= sum(penalty))
    # solver.Add(suma_wT >= sum((starts[i] + jobs[i].P - jobs[i].D) * jobs[i].W if (starts[i] + jobs[i].P - jobs[i].D) >= 0 else 0 for i in range(len(jobs))))

    solver.Minimize(suma_wT)
    status = solver.Solve()
    if status != pywraplp.Solver.OPTIMAL:
        print("Not optimal!")
    print(instanceName, "Suma opt:", solver.Objective().Value())
    pi = [(i, starts[i].solution_value()) for i in range(len(starts))]

    pi.sort(key=lambda x: x[1])
    print(pi)


def GetPWDsFromFile (file_path):

    full_file = Path(file_path).read_text()
    words = full_file.replace("\n", " ").split(" ")
    words_cleaned = list(filter(None, words))
    numbers = list(map(int, words_cleaned))

    jobs = []
    for i in range(numbers.pop(0)):
        jobs.append(PWD(numbers[0], numbers[1], numbers[2]))
        numbers.pop(0)
        numbers.pop(0)
        numbers.pop(0)
    return jobs


if __name__ == '__main__':
    files = ["./dane pwd/data1.txt"]
    for file in files:
        jobs = GetPWDsFromFile(file)
        Milp_WT(jobs, file)
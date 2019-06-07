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


def CP_WT(jobs, instanceName):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()
    sumaP = [job.P for job in jobs]
    variableMaxValue = sum(job.W*(sum(sumaP)-job.D) if sum(sumaP)-job.D > 0 else 0 for job in jobs)

    starts = [(model.NewIntVar(0, variableMaxValue, "starts"+str(i))) for i in range(len(jobs))]
    penalty = [(model.NewIntVar(0, variableMaxValue, "kara" + str(i))) for i in range(len(jobs))]

    alfasMatrix = {}
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = model.NewIntVar(0, 1, "alfa"+str(i) + "_" + str(j))

    for i in range(len(jobs)):
        for j in range(i+1, len(jobs)):
            model.Add(starts[i]+jobs[i].P <= starts[j] + alfasMatrix [i,j]*variableMaxValue)
            model.Add(starts[j]+jobs[j].P <= starts[i] + alfasMatrix[j,i] *variableMaxValue)
            model.Add(alfasMatrix[i,j] + alfasMatrix[j,i] == 1)

    model.Minimize(sum((starts[i]+jobs[i].P-jobs[i].D)*jobs[i].W if (starts[i]+jobs[i].P-jobs[i].D) >= 0 else 0 for i in range(len(starts))))
    status = solver.Solve(model)
    pi = [(i, start.GetVarValueMap()) for start in starts]
    print(instanceName, "Suma opt:", solver.ObjectiveValue())

    pi.sort(key=lambda x: x[1])
    print(pi)


def Milp_WT(jobs, instanceName):
    solver = pywraplp.Solver('simple_mip_program',
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)
    sumaP = []
    for x in range(len(jobs)):
        sumaP.append(jobs[x].P)
    variableMaxValue = sum(job.W*(sum(sumaP)-job.D) if sum(sumaP)-job.D > 0 else 0 for job in jobs)

    starts = [(solver.IntVar(0, variableMaxValue, "starts"+str(i))) for i in range(len(jobs))]
    penalty = [(solver.IntVar(0, variableMaxValue, "kara" + str(i))) for i in range(len(jobs))]

    alfasMatrix = {}
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = solver.IntVar(0, 1, "alfa"+str(i) + "_" + str(j))

    for i in range(len(jobs)):
        for j in range(i+1, len(jobs)):
            solver.Add(starts[i]+jobs[i].P <= starts[j] + alfasMatrix [i,j]*variableMaxValue)
            solver.Add(starts[j]+jobs[j].P <= starts[i] + alfasMatrix[j,i] *variableMaxValue)
            solver.Add(alfasMatrix[i,j] + alfasMatrix[j,i] == 1)
        solver.Add(penalty[i] >= (starts[i]+jobs[i].P-jobs[i].D)*jobs[i].W)

    solver.Minimize(sum(penalty))
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
    files = ["./dane pwd/data11.txt"]
    for file in files:
        jobs = GetPWDsFromFile(file)
        # CP_WT(jobs, file)
        Milp_WT(jobs, file)
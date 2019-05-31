from __future__ import print_function
from ortools.linear_solver import pywraplp
from pathlib import Path
from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import solver_parameters_pb2


def cp(jobs, instanceName):
    variableMaxValue = sum(job.R + job.P + job.Q for job in jobs)
    # Instantiate a CP solver.
    parameters = pywrapcp.Solver.DefaultSolverParameters()
    solver = pywrapcp.Solver('simple_CP', parameters)
    m
    alfasMatrix = {}
    for i in range(len(jobs)):
      for j in range(len(jobs)):
          alfasMatrix[i, j] = solver.IntVar(0, 1, "alfa" + str(i) + "_" + str(j))

    starts = [(solver.IntVar(0, variableMaxValue, "starts" + str(i))) for i in range(len(jobs))]
    cmax = solver.IntVar(0, variableMaxValue, "cmax")

    for job, start in zip(jobs, starts):
      solver.Add(start >= job.R)
      solver.Add(cmax >= start + job.P + job.Q)

    for i in range(len(jobs)):
      for j in range(i + 1, len(jobs)):
          solver.Add(starts[i] + jobs[i].P <= starts[j] + alfasMatrix[i, j] * variableMaxValue)
          solver.Add(starts[j] + jobs[j].P <= starts[i] + alfasMatrix[j, i] * variableMaxValue)
          solver.Add(alfasMatrix[i, j] + alfasMatrix[j, i] == 1)

    model.Minimize(cmax)
    status = solver.Solve()
    if status != pywraplp.Solver.OPTIMAL:
      print("Not optimal!")
    print(instanceName, "Cmax:", solver.Objective().Value())
    pi = [(i, starts[i].solution_value()) for i in range(len(starts))]

    pi.sort(key=lambda x: x[1])
    print(pi)


class RPQ():
    def __init__(self, r, p, q):
        self.R = r
        self.P = p
        self.Q = q


def Milp(jobs, instanceName):
    variableMaxValue = sum(job.R+job.P+job.Q for job in jobs)

    solver = pywraplp.Solver('simple_mip_program',
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    alfasMatrix = {}
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = solver.IntVar(0, 1, "alfa"+str(i) + "_" + str(j))

    starts = [(solver.IntVar(0, variableMaxValue, "starts"+str(i))) for i in range(len(jobs))]
    cmax = solver.IntVar(0, variableMaxValue, "cmax")

    for job, start in zip(jobs, starts):
        solver.Add(start >= job.R)
        solver.Add(cmax >= start + job.P + job.Q)

    for i in range(len(jobs)):
        for j in range(i+1, len(jobs)):
            solver.Add(starts[i]+jobs[i].P <= starts[j] + alfasMatrix [i,j]*variableMaxValue)
            solver.Add(starts[j]+jobs[j].P <= starts[i] + alfasMatrix[j,i] *variableMaxValue)
            solver.Add(alfasMatrix[i,j] + alfasMatrix[j,i] == 1)

    solver.Minimize(cmax)
    status = solver.Solve()
    if status != pywraplp.Solver.OPTIMAL:
        print("Not optimal!")
    print(instanceName, "Cmax:", solver.Objective().Value())
    pi = [(i, starts[i].solution_value()) for i in range(len(starts))]

    pi.sort(key=lambda x: x[1])
    print(pi)


def GetRPQsFromFile (file_path):

    full_file = Path(file_path).read_text()
    words = full_file.replace("\n", " ").split(" ")
    words_cleaned = list(filter(None, words))
    numbers = list(map(int, words_cleaned))

    jobs = []
    for i in range(numbers.pop(0)):
        jobs.append(RPQ(numbers[0], numbers[1], numbers[2]))
        numbers.pop(0)
        numbers.pop(0)
        numbers.pop(0)
    return jobs


if __name__ == '__main__':
    files = ["./dane rpq/data000.txt"]
    for file in files:
        jobs = GetRPQsFromFile(file)
        cp(jobs, file)
        Milp(jobs, file)

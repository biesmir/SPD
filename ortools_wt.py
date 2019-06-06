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
    print("sumaP" + str(sum(sumaP)))
    variableMaxValue = sum(job.W*(sum(sumaP)-job.D) for job in jobs)
    print(variableMaxValue)
    solver = pywraplp.Solver('simple_mip_program',
            pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

    alfasMatrix = {}
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = solver.IntVar(0, 1, "alfa"+str(i) + "_" + str(j))

    starts = [(solver.IntVar(0, variableMaxValue, "starts"+str(i))) for i in range(len(jobs))]
    delay = [(solver.IntVar(0, variableMaxValue, "delay" + str(i))) for i in range(len(jobs))]
    suma_wT = solver.IntVar(0, variableMaxValue, "suma_wT")

    # Ti = []
    # sumaP2 = []
    # list2 = []
    #
    # for x in range(len(jobs)):
    #     sumaP2.append(jobs[x].P)
    #     if sum(sumaP2) > jobs[x].D:
    #         Ti.append(sum(sumaP2) - jobs[x].D)
    #         # print(sumaP)
    #         # print(sum(sumaP))
    #         # print(jobs[x].D)
    #     else:
    #         Ti.append(0)
    #     list2.append(jobs[x].W * Ti[x])
    #     suma = sum(list2)
    #
    # print(suma)
    # print(list2)
    # lista = []
    suma = []
    s_2 = []
    for job, start in zip(jobs, starts):
        for i in range(len(jobs)):
            solver.Add(start >= job.P)
            suma.append(jobs[i].P)
            #solver.Add(suma_wT >= suma)
            solver.Add(delay[i] >= sum(suma) - job.D)
            #solver.Add(jobs[i-1].P >= jobs[i].P)
            # s_2.append(delay[i]*job.W)
            # solver.Add(suma_wT >= sum(s_2))

        # for i in range(len(jobs)):
        #     for j in range(i + 1, len(jobs)):
        #         solver.Add(starts[i] + jobs[i].P <= starts[j] + alfasMatrix[i, j] * variableMaxValue)
        #         solver.Add(starts[j] + jobs[j].P <= starts[i] + alfasMatrix[j, i] * variableMaxValue)
        #         solver.Add(alfasMatrix[i, j] + alfasMatrix[j, i] == 1)

    #     lista.append(job.P)
    # K = []
    # for x in range(len(jobs)):
    #     K.append(jobs[x].W*(sum(lista)-jobs[x].D))
    #     kopia = lista
    #     kopia.remove(jobs[x].P)


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
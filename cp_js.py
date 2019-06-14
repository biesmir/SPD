from ortools.sat.python import cp_model


class Job:
    def __init__(self, machine, time):
        self.machine = machine
        self.time = time


def load_from_file(file_name):
    joblist = []
    with open(file_name) as file:
        line = file.readline()
        line = list(map(int, line.split()))
        groups_number = line[0]
        machine_number = line[1]

        for i in range(groups_number):
            line = file.readline()
            line = list(map(int, line.split()))
            group = []
            for j in range(machine_number):
                group.append(Job(line[2*j+1], line[2*j+2]))
            joblist.append(tuple(group))

    return tuple(joblist), machine_number


def cp_js(jobs, machines):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    variableMaxValue = 0
    for group in jobs:
        for job in group:
            variableMaxValue += job.time
    alfasList = []
    for k in range(machines):
        alfasMatrix = {}
        for i in range(machines):
            for j in range(machines):
                alfasMatrix[i, j] = model.NewIntVar(0, 1, "alfa"+str(i) + "_" + str(j)+ "_" + str(k))

        alfasList.append(alfasMatrix)

    starts = [[(model.NewIntVar(0, variableMaxValue, "starts"+str(i)+"machine"+str(j))) for i in range(len(jobs))] for j in range(machines)]
    cmax = model.NewIntVar(0, variableMaxValue, "cmax")

    for i in range(len(jobs)):
        for j in range(1, len(jobs[0])):
            model.Add(starts[i][j] >= starts[i][j-1] + jobs[i][j-1].time)
            model.Add(cmax >= starts[i][j] + jobs[i][j].time)

    for k in range(len(alfasList)):
        for i in range(len(jobs)):
            for j in range(i+1, len(jobs)):
                model.Add(alfasList[k][i, j] + alfasList[k][j, i] == 1)
                for m in range(len(jobs[j])):
                    if jobs[j][m].machine == k + 1:
                        break
                for l in range(len(jobs[i])):
                    if jobs[i][l].machine == k + 1:
                        break
                model.Add(starts[i][l] + jobs[i][l].time <= starts[j][m] + alfasList[k][i, j]*variableMaxValue)
                model.Add(starts[j][m] + jobs[j][m].time <= starts[i][l] + alfasList[k][j, i]*variableMaxValue)


    model.Minimize(cmax)
    status = solver.Solve(model)
    pi = [(i, starts[i][0].GetVarValueMap()) for i in range(len(starts))]
    # pi.sort(key=lambda x: x[1])
    print(pi)
    cmax.GetVarValueMap()
    print(solver.ObjectiveValue())
    return


if __name__ == '__main__':
    jobs, machines = load_from_file("insa/data001.txt")
    cp_js(jobs, machines)

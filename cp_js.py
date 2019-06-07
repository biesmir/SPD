from ortools.sat.python import cp_model
from job import Job


def load_from_file(file_name):
    joblist = []
    with open(file_name) as file:
        line = file.readline()
        line = file.readline()
        while "data" not in line:
            pass
            line = file.readline()
        line = file.readline()
        line = list(map(int, line.split()))

        for i, line in enumerate(file.readlines()):
            if line != '\n':
                joblist.append(Job(list(map(int, line.split())), index=i, name="zadanie " + str(i + 1)))
    return joblist


def cp_js(jobs):
    model = cp_model.CpModel()
    solver = cp_model.CpSolver()

    variableMaxValue = sum(job.time[i] for i in range(len(jobs[0].time)) for job in jobs )

    alfasMatrix = {}
    for i in range(len(jobs)):
        for j in range(len(jobs)):
            alfasMatrix[i, j] = model.NewIntVar(0, 1, "alfa"+str(i) + "_" + str(j))

    starts = [[(model.NewIntVar(0, variableMaxValue, "starts"+str(i)+"machine"+str(j))) for i in range(len(jobs[0].time))] for j in range(len(jobs))]
    cmax = model.NewIntVar(0, variableMaxValue, "cmax")

    for i in range(len(jobs)):
        for j in range(i+1, len(jobs)):
            for k in range(len(jobs[0].time)):
                model.Add(starts[i][k]+jobs[i].time[k] <= starts[j][k] + alfasMatrix [i,j]*variableMaxValue)
                model.Add(starts[j][k]+jobs[j].time[k] <= starts[i][k] + alfasMatrix[j,i] *variableMaxValue)
                model.Add(alfasMatrix[i,j] + alfasMatrix[j,i] == 1)
        model.Add(cmax >= starts[i][k] + jobs[i].time[k])

    model.Minimize(cmax)
    status = solver.Solve(model)
    pi = [(i, starts[i][0].GetVarValueMap()) for i in range(len(starts))]
    # pi.sort(key=lambda x: x[1])
    print(pi)
    # cmax.GetVarValueMap()
    print(solver.ObjectiveValue())


if __name__ == '__main__':
    jobs = load_from_file("insa/ta01")
    cp_js(jobs)

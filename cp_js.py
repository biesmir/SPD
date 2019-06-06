from ortools.sat.python import cp_model
from job import Job
from ortools.linear_solver import pywraplp


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

    starts = [[(model.NewIntVar(0, variableMaxValue, "starts"+str(i)+"machine"+str(j))) for i in range(len(jobs))] for j in range(len(jobs))]
    cmax = model.NewIntVar(0, variableMaxValue, "cmax")

    for j in range(1, len(jobs[0].time)):
        model.Add(starts[0][j] >= jobs[0].time[j-1] + starts[0][j-1])

    for i in range(1, len(jobs)):
        for j in range(1, len(jobs[0].time)):
            model.Add(starts[i][j] >= jobs[i-1].time[j-1] + starts[i-1][j])
            model.Add(starts[i][j] >= jobs[i-1].time[j-1] + starts[i][j-1])
    model.Add(cmax >= starts[-1][-1] + jobs[-1].time[-1])

    model.Minimize(cmax)
    status = solver.Solve(model)
    if status != pywraplp.Solver.OPTIMAL:
        print("Not optimal!")

    print(solver.ObjectiveValue())


if __name__ == '__main__':
    jobs = load_from_file("ta0")
    cp_js(jobs)

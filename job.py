class Job:

    def __init__(self, time):
        self.time = tuple(time)

    def __str__(self):
        line = self.name + "    | "
        for i in self.time:
            line += str(i) + " | "
        return line

    def __repr__(self):
         return self.name

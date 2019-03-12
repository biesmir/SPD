class Job:

    def __init__(self, time, name="zadanie"):
        self.time = tuple(time)
        self.name = name

    def __str__(self):
        line = self.name + "    | "
        for i in self.time:
            line += str(i) + " | "
        return line

    def __repr__(self):
         return self.name

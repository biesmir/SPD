class Job:

    def __init__(self, time, index, name="zadanie"):
        self.time = tuple(time)
        self.name = name
        self.index = index

    def __str__(self):
        line = self.name + "    | "
        for i in self.time:
            line += str(i) + " | "
        return line

    def __repr__(self):
        line = self.name + "    | "
        for i in self.time:
            line += str(i) + " | "
        return line

    def __le__(self, second):
        if self.time[0] <= second.time[0] & self.time[0] <= second.time[1]:
            return True
        if self.time[1] <= second.time[0] & self.time[1] <= second.time[1]:
            return True
        else:
            return False

    def __lt__(self, second):
        if self.time[0] < second.time[0] and self.time[0] < second.time[1] or \
         self.time[1] < second.time[0] and self.time[1] < second.time[1]:
            return True
        else:
            return False

class HeapQ:
    """
    max heap
    """
    def __init__(self, schdl=[]):
        self.array = []
        self.size = 0
        if schdl != []:
            for job in schdl.job_list:
                self.push(job)

    def push(self, job):
        if not self.array:
            self.array.append(job)
        else:
            self.array.append(job)
            self.size = len(self.array)
            index = self.size - 1
            parent = int((index - 1) / 2)
            while index != 0 and self.array[parent].q < self.array[index].q:

                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                index = parent
                parent = int((index - 1) / 2)

    def pop(self):
        value = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size = len(self.array) - 1
        index = 0
        while index*2 + 1 <= self.size:
            if index*2 + 2 <= self.size:
                if self.array[index * 2 + 2].q > self.array[index * 2 + 1].q:
                    bigger = index * 2 + 2
                else:
                    bigger = index * 2 + 1
            else:
                bigger = index * 2 + 1
            if self.array[index].q > self.array[bigger].q:
                break
            else:
                self.array[bigger], self.array[index] = self.array[index], self.array[bigger]
                index = bigger

        return value


class HeapR:
    """
    min heap
    """
    def __init__(self, schdl):
        self.array = []
        self.size = 0
        if schdl != []:
            for job in schdl.job_list:
                self.push(job)

    def push(self, job):
        if not self.array:
            self.array.append(job)
        else:
            self.array.append(job)
            self.size = len(self.array)
            index = self.size - 1
            parent = int((index - 1) / 2)
            while index != 0 and self.array[parent].r > self.array[index].r:

                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                index = parent
                parent = int((index - 1) / 2)

    def pop(self):
        value = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size = len(self.array) - 1
        index = 0
        while index*2 + 1 < self.size:
            if self.array[index * 2 + 2].r < self.array[index * 2 + 1].r:
                smaller = index * 2 + 2
            else:
                smaller = index * 2 + 1
            if self.array[index].r < self.array[smaller].r:
                break
            else:
                self.array[smaller], self.array[index] = self.array[index], self.array[smaller]
                index = smaller

        return value

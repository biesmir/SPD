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
            self.size = len(self.array)
            self.array.append(job)
            index = self.size
            parent = int((index - 1) / 2)
            while index != 0 and self.array[parent].q < self.array[index].q:

                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                parent = int((index - 1) / 2)

    def pop(self):
        value = self.array[0]

        del self.array[0]
        self.size = len(self.array)
        index = 0
        while index < self.size and index * 2 + 1 < self.size:
            if self.array[index].q < self.array[index * 2 + 1].q:
                self.array[index * 2 + 1], self.array[index] = self.array[index], self.array[index * 2 + 1]
                index = index * 2 + 1

            elif index * 2 + 2 < self.size:
                if self.array[index].q < self.array[index * 2 + 2].q:
                    self.array[index * 2 + 2], self.array[index] = self.array[index], self.array[index * 2 + 2]
                    index = index * 2 + 2

                else:
                    break

            else:
                break

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
            self.size = len(self.array)
            self.array.append(job)
            index = self.size
            parent = int((index - 1) / 2)
            while index != 0 and self.array[parent].r > self.array[index].r:

                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                parent = int((index - 1) / 2)

    def pop(self):
        value = self.array[0]
        del self.array[0]
        self.size = len(self.array)
        index = 0
        while index < self.size * index*2 + 1 < self.size:
            if self.array[index].r > self.array[index * 2 + 1].r:
                self.array[index * 2 + 1], self.array[index] = self.array[index], self.array[index * 2 + 1]
                index = index * 2 + 1

            elif index*2 + 2 < self.size:
                if self.array[index].r > self.array[index * 2 + 2].r:
                    self.array[index * 2 + 2], self.array[index] = self.array[index], self.array[index * 2 + 2]
                    index = index * 2 + 2
                else:
                    break

            else:
                break

        return value


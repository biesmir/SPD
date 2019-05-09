class HeapQ:
    """
    max heap
    """
    def __init__(self, schdl):
        self.array = []
        self.size = 0
        for job in schdl.job_list:
            self.push(job)

    def push(self, job):
        if not self.array:
            self.array.append(job)
        else:
            self.size += 1
            self.array.append(job)
            index = self.size
            parent = int((index - 1) / 2)
            while index != 0 and self.array[parent].q < self.array[index].q:

                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                parent = int((index - 1) / 2)

    def pop(self):
        value = self.array[0]
        self.size -= 1
        del self.array[0]
        index = 0
        while index < self.size:
            if self.array[index].q < self.array[index * 2 + 1].q:
                self.array[index * 2 + 1], self.array[index] = self.array[index], self.array[index * 2 + 1]
                index = index * 2 + 1

            elif self.array[index].q < self.array[index * 2 + 2].q:
                self.array[index * 2 + 2], self.array[index] = self.array[index], self.array[index * 2 + 2]
                index = index * 2 + 2

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
        for job in schdl.job_list:
            self.push(job)

    def push(self, job):
        if not self.array:
            self.array.append(job)
        else:
            self.size += 1
            self.array.append(job)
            index = self.size
            parent = int((index - 1) / 2)
            while index != 0 and self.array[parent].r > self.array[index].r:

                self.array[parent], self.array[index] = self.array[index], self.array[parent]
                parent = int((index - 1) / 2)

    def pop(self):
        value = self.array[0]
        self.size -= 1
        del self.array[0]
        index = 0
        while index < self.size:
            if self.array[index].r > self.array[index * 2 + 1].r:
                self.array[index * 2 + 1], self.array[index] = self.array[index], self.array[index * 2 + 1]
                index = index * 2 + 1

            elif self.array[index].r > self.array[index * 2 + 2].r:
                self.array[index * 2 + 2], self.array[index] = self.array[index], self.array[index * 2 + 2]
                index = index * 2 + 2

            else:
                break

        return value


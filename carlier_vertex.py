class Vertex:
    def __init__(self, schdl, depth, lb, ub):
        self.schdl = schdl
        self.depth = depth
        self.lb = lb
        self.ub = ub

    def __lt__(self, other):
        if self.depth > other.depth:
            return True
        elif self.depth == other.depth:
            if self.lb < other.lb:
                return True
        else:
            return False

class Vertex:
    def __init__(self, schdl, depth, ub):
        self.schdl = schdl
        self.depth = depth
        self.ub = ub

    def __lt__(self, other):
        if self.depth > other.depth:
            return True
        elif self.depth == other.depth:
            if self.ub < other.ub:
                return True
        else:
            return False

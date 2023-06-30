class Graph:
    def __init__(self, file_name):
        self.file_name = file_name
        self.v = 0
        self.e = 0
        self.edges = []

        self.tau_min = 0.01
        self.tau_max = 6

        self.create_graph()

    def read_file(self):

        with open(self.file_name, "r") as f:
            for line in f:
                if line[0] == "p":
                    self.v = int(line.strip().split()[2])
                    self.e = int(line.strip().split()[3])
                if line[0] == "e":
                    a = int(line.strip().split()[1])
                    b = int(line.strip().split()[2])
                    ab = (min(a, b), max(a, b))
                    self.edges.append(ab)

    def create_graph(self):
        self.read_file()

        dict = {}
        for i in range(1, self.v+1):
            dict[i] = []

        for t in self.edges:
            a, b = t
            dict[a].append(b)
            dict[b].append(a)

        self.edges = dict

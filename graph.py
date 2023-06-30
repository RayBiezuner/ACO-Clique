from vertex import Vertex

class Graph:
    def __init__(self, file_name):
        self.vertex_list = []
        self.create_graph(file_name)
        self.tau_min = 0.01
        self.tau_max = 6
        self.v = 0
        self.e = 0

    def create_graph(self,file_name):

        with open(file_name, "r") as f:
            for line in f:
                if line[0] == "p":
                    self.v = int(line.strip().split()[2])
                    self.vertex_list = [None] * 500
                    self.e = int(line.strip().split()[3])
                if line[0] == "e":
                    a = int(line.strip().split()[1])
                    b = int(line.strip().split()[2])

                    if self.vertex_list[a] == None:
                        self.vertex_list[a] = Vertex(0)

                    if self.vertex_list[b] == None:
                        self.vertex_list[b] = Vertex(0)

                    self.vertex_list[a].append_adj(self.vertex_list[b])          
                    self.vertex_list[b].append_adj(self.vertex_list[a])

                    

from vertex import Vertex

class Graph:
    def __init__(self, file_name):
        self.vertex_list = []
        self.tau_min = 0.01
        self.tau_max = 6
        self.v = 0
        self.e = 0
        self.create_graph(file_name)

    def create_graph(self,file_name):

        with open(file_name, "r") as f:
            for line in f:
                if line[0] == "p":
                    self.v = int(line.strip().split()[2])
                    self.vertex_list = [None] * self.v
                    self.e = int(line.strip().split()[3])
                if line[0] == "e":
                    a = int(line.strip().split()[1])
                    b = int(line.strip().split()[2])
                    a=a-1
                    b=b-1
                    if self.vertex_list[a] == None:
                        self.vertex_list[a] = Vertex(self.tau_min)

                    if self.vertex_list[b] == None:
                        self.vertex_list[b] = Vertex(self.tau_min)

                    self.vertex_list[a].addNeighbour(self.vertex_list[b])          
                    self.vertex_list[b].addNeighbour(self.vertex_list[a])
    
    def restart(self):
        for vertex in self.vertex_list:
            vertex.pheromone_value = self.tau_min    
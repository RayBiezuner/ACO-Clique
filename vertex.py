class Vertex:
    def __init__(self, pheromone_value):
        self.adjacency_list = []
        self.pheromone_value = pheromone_value
    
    def expands(self):
        return self.adjacency_list
    
    def append_adj(self,vertex):
        self.adjacency_list.append(vertex)
class Vertex:
    def __init__(self, index, pheromone_value):
        self.adjacency_list = []
        self.index = index
        self.pheromone_value = pheromone_value
    
    def expands(self):
        return set(self.adjacency_list)
    
    def append_adj(self,vertex):
        self.adjacency_list.append(vertex)
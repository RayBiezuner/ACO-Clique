class Vertex:
    def __init__(self, adjacency_list, index, pheromone_value):
        self.adjacency_list = adjacency_list
        self.index = index
        self.pheromone_value = pheromone_value
    
    def expands(self):
        return set(self.adjacency_list)
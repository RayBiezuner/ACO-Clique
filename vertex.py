class Vertex:
    def __init__(self, pheromone_value):
        self.neighbours = []
        self.pheromone_value = pheromone_value
    
    def expands(self):
        return self.neighbours
    
    def addNeighbour(self, vertex):
        self.neighbours.append(vertex)
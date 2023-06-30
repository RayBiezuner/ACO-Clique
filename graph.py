from vertex import Vertex

class Graph:
    def __init__(self):
        self.vertex = []

    def add_edge(self, adjacency_list, index, pheromone_value):
        vertex = Vertex(adjacency_list, index, pheromone_value)
        self.edges.append(vertex)
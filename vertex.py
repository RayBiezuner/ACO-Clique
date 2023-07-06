class Vertex:
    """
    Classe que representa um vértice em um grafo.
    """
    def __init__(self, pheromone_value):
        """
        Inicializa a classe Vertex.

        :param pheromone_value: Valor do feromônio associado ao vértice.
        """
        self.neighbours = []
        self.pheromone_value = pheromone_value
    
    def expands(self):
        """
        Retorna os vértices vizinhos.

        :return: Lista de vértices vizinhos.
        """
        return self.neighbours
    
    def addNeighbour(self, vertex):
        """
        Adiciona um vértice vizinho.

        :param vertex: Vértice vizinho a ser adicionado.
        """
        self.neighbours.append(vertex)
        
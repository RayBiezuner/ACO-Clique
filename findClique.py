import random
from graph import Graph
from vertex import Vertex
import time
from configuration import *



configuration = Config.get_instance()
alpha = configuration.parameters["alpha"]
optimal = configuration.parameters["optimal"]
max_iterations = configuration.parameters["iterations"]
num_ants = configuration.parameters["num_ants"]
evaportation_hate = configuration.parameters["evaporation"]


def p(v_i : Vertex,Candidates: set[Vertex]):
    """
    Calcula a probabilidade de escolha de um vértice v_i em relação a um conjunto de candidatos.

    :param v_i: Vértice v_i para o qual a probabilidade será calculada.
    :param Candidates: Conjunto de vértices candidatos.
    :return: Probabilidade de escolha do vértice v_i.
    """
    denominator = sum(candidate.pheromone_value for candidate in Candidates)
    return v_i.pheromone_value/(denominator**alpha)

def updatePheromone(clique,pheromone,max):
    """
    Atualiza o valor do feromônio nos vértices de um clique.

    :param clique: Lista de vértices que compõem o clique.
    :param pheromone: Valor do feromônio a ser adicionado.
    :param max: Valor máximo permitido para o feromônio de um vértice.
    """
    for vertex in clique:
        vertex.pheromone_value += pheromone
        if vertex.pheromone_value > max: #verifica de o novo valor é maior que o máximo
            vertex.pheromone_value = max

def evaporatePheromone(graph):
    """
    Realiza a evaporação do feromônio em todos os vértices do grafo.
    :param graph: Grafo contendo os vértices com feromônio a ser evaporado.
    """
    for vertex in graph.vertex_list:
        vertex.pheromone_value *= (1.0 - configuration.parameters["evaporation"])
        if vertex.pheromone_value < graph.tau_min: #verifica se o novo valor é menor do que o mínimo
            vertex.pheromone_value = graph.tau_min


def findClique(G: Graph):
    """
    Encontra o clique máximo em um grafo utilizando o algoritmo de Otimização por Colônia de Formigas (ACO).

    :param G: Grafo no qual será buscado o clique máximo.
    :return: Maior clique encontrado, número de iterações realizadas e tempo de execução.
    """

    start = time.time()
    Candidates = []
    largest_clique = [] 
    vector_cliques = []
    clique= []
    it=0
    while it<max_iterations and len(largest_clique) != optimal:
        for k in range(num_ants):
            v_i = random.choice(G.vertex_list) 
            clique = []
            clique.append(v_i)
            Candidates = Candidates + v_i.expands()
            while(len(Candidates) != 0):
                prob = [p(v,Candidates) for v in Candidates]
                v_i = random.choices(Candidates,weights = prob, k =1)[0]
                clique.append(v_i)
                Candidates = list(set(Candidates) & set(v_i.expands()))
            vector_cliques.append(clique)
            evaporatePheromone(G) 
            if(len(clique) > len(largest_clique)):
                largest_clique = clique
            pheromone = 1/(1+len(largest_clique) - len(clique))
            updatePheromone(clique,pheromone,G.tau_max)
        it+=1 
    print("Finish") #Apenas adicionado para que tenha algum indicativo de que uma run foi encerrada
    end = time.time()
    return largest_clique,it,end-start






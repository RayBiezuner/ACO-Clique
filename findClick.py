from graph import Graph
from vertex import Vertex
import random
alpha = 1
max_cicles = 100000
def p(v_i : Vertex,Candidates: set[Vertex]):
    denominator = sum(candidate.pheromon_value for candidate in Candidates)
    return v_i.pheromone_value/(denominator**alpha)

def update_pheromone(click,pheromone):
    for vertex in click:
        vertex.pheromone_valur += pheromone

        
def findClick(G: Graph):
    Candidates = []
    Click = []
    largest_click = []
    Ants = []
    i=0
    while i<max_cicles:
        k=0
        for k in range(len(Ants)):
            v_i = random.choice(G.vertex) 
            Click[k].append(v_i)
            Candidates = set(Candidates + v_i.expands())
            while(len(Candidates) != 0):
                prob = [p(v) for v in Candidates]
                v_i = random.choices(Candidates,weights = prob, k =1)[0]
                Click[k].append(v_i)
                Candidates = Candidates & v_i.expands()
        for click in Click:
            pheromone = 1/(1+len(largest_click) - len(click))
            update_pheromone(click,pheromone)
            if(len(click) > len(largest_click)):
                largest_click = click
    i+=1  
    return largest_click

    





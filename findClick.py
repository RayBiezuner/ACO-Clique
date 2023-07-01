import random
from graph import Graph
from vertex import Vertex
from configuration import *

configuration = Config.get_instance()
alpha = configuration.parameters["alpha"]
max_iterations = configuration.parameters["iterations"]
num_ants = configuration.parameters["num_ants"]
evaportation_hate = configuration.parameters["evaporation"]

def p(v_i : Vertex,Candidates: set[Vertex]):
    denominator = sum(candidate.pheromone_value for candidate in Candidates)
    return v_i.pheromone_value/(denominator**alpha)

def update_pheromone(click,pheromone):
    for vertex in click:
        vertex.pheromone_value += pheromone


def findClick(G: Graph):
    Candidates = []
    vector_clicks = []
    largest_click = [] 
    click= []
    i=0
    while i<max_iterations:
        k=0
        for k in range(num_ants):
            v_i = random.choice(G.vertex_list) 
            click = []
            click.append(v_i)
            Candidates = Candidates + v_i.expands()
            while(len(Candidates) != 0):
                prob = [p(v,Candidates) for v in Candidates]
                v_i = random.choices(Candidates,weights = prob, k =1)[0]
                click.append(v_i)
                Candidates = list(set(Candidates) & set(v_i.expands()))
            vector_clicks.append(click)
        
            
        for click in vector_clicks:
            if(len(click) > len(largest_click)):
                largest_click = click
            pheromone = 1/(1+len(largest_click) - len(click))
            update_pheromone(click,pheromone)
        i+=1 
    
     
    return largest_click

    





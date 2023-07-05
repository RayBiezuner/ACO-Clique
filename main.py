from graph import Graph
from findClick import findClick
import sys
from configuration import *
arguments = sys.argv
import random
import math

def calcular_media_desvio_padrao(lista):
    n = len(lista)
    if n < 2:
        raise ValueError("A lista deve conter pelo menos 2 elementos.")
    
    media = sum(lista) / n
    soma_diferencas_quadrado = sum((x - media) ** 2 for x in lista)
    variancia = soma_diferencas_quadrado / (n - 1)
    desvio_padrao = math.sqrt(variancia)
    
    return media, desvio_padrao
def main():
    results=[]
    config = Config.get_instance()
    for it in range(30):
        print("seed: ",it,":")
        graph = Graph('800_207643.txt')
        random.seed(it)
        results.append(len(findClick(graph)))
    print("RESULTADOS:")
    print(results)
    media,desvio = calcular_media_desvio_padrao(results)
    print(f"Media: {media} \n Desvio: {desvio}")
    
if __name__ == "__main__":
    main()
from graph import Graph
from findClique import findClique
from configuration import *

def logger(mensagem):
    """
    Registra uma mensagem em um arquivo de log.

    :param mensagem: Mensagem a ser registrada.
    """
    config = Config.get_instance()
    file_name = f"log-it{config.parameters['iterations']}na{config.parameters['num_ants']}alpha{config.parameters['alpha']}ev{config.parameters['evaporation']}"
    with open(f"{file_name}.txt", "a") as arquivo_log:
        arquivo_log.write(mensagem+ "\n")
        
def main():
    """
    Função principal que executa o algoritmo para encontrar o clique máximo em um grafo.
    """
    config = Config.get_instance()
    input = '700_121728.txt'
    logger(f"input: {input}\nMaximo de Iteracoes : {config.parameters['iterations']}\nFormigas: {config.parameters['num_ants']}\nTaxa de evaporacao: {config.parameters['evaporation']}\nAlpha: {config.parameters['alpha']}")
    graph = Graph(input)
    for run in range(30):
        clique,it,time = findClique(graph)
        size = len(clique)
        logger(f"{run};{size}")
        graph.restart()
    

if __name__ == "__main__":
    main()
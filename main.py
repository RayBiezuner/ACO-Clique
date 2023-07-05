from graph import Graph
from findClique import findClick
import sys
from configuration import *
arguments = sys.argv

def main():
    config = Config.get_instance()
<<<<<<< HEAD
    graph = Graph('800_207643.txt')
=======
    graph = Graph('500_62624.txt')
>>>>>>> ce7339daada2f211a536fa7dd962ceb5d0cf07b9
    print(f"Tamanho = {len(findClick(graph))}")

if __name__ == "__main__":
    main()
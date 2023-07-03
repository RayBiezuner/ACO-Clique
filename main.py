from graph import Graph
from findClique import findClick
import sys
from configuration import *
arguments = sys.argv

def main():
    config = Config.get_instance()
    graph = Graph('500_62624.txt')
    print(f"Tamanho = {len(findClick(graph))}")

if __name__ == "__main__":
    main()
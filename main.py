from graph import Graph
from findClick import findClick
import sys
from configuration import *
arguments = sys.argv

def main():
    config = Config.get_instance()
    graph = Graph('700_121728.txt')
    print(f"Tamanho = {len(findClick(graph))}")

if __name__ == "__main__":
    main()
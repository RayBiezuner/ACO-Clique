from graph import Graph
from findClick import findClick
import vertex


def main():
    graph = Graph('700_121728.txt')
    print(f"Tamanho = {len(findClick(graph,30))}")

if __name__ == "__main__":
    main()
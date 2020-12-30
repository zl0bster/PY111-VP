from typing import Hashable, List
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def show_graph(g: nx.Graph):
    nx.draw(g, with_labels=True)
    plt.show()


def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an breadth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node for search
    :return: list of nodes in the visited order
    """
    visited = {node: False for node in g.nodes}
    path = []
    waitNodes = deque()
    waitNodes.append(start_node)
    visited[start_node] = True
    while waitNodes:
        currentNode = waitNodes.popleft()
        path.append(currentNode)
        for neighbour in g.neighbors(currentNode):
            if not visited[neighbour]:
                waitNodes.append(neighbour)
                visited[neighbour] = True

    return path


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFGHIJ")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'F'),
        ('B', 'G'),
        ('F', 'G'),
        ('G', 'C'),
        ('G', 'H'),
        ('G', 'I'),
        ('C', 'H'),
        ('I', 'H'),
        ('H', 'D'),
        ('H', 'E'),
        ('H', 'J'),
        ('E', 'D'),
    ])
    print(graph.nodes)
    print(graph['A'])  # dict
    print(list(graph.neighbors('A')))
    # show_graph(graph)
    print(bfs(graph, 'A'))

from typing import Hashable, List
import networkx as nx
from collections import deque
import matplotlib.pyplot as plt


def show_graph(g: nx.Graph):
    nx.draw(g, with_labels=True)
    plt.show()


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    """
    Do an depth-first search and returns list of nodes in the visited order

    :param g: input graph
    :param start_node: starting node of search
    :return: list of nodes in the visited order
    """
    visitedNodes = {node: False for node in g.nodes}
    path = [start_node]
    visitedNodes[start_node] = True
    waitingNodes = [start_node]
    while waitingNodes:
        currentNode = waitingNodes[-1]
        if all(visitedNodes[node] for node in g.neighbors(currentNode)):
            waitingNodes.pop()
            continue
        for node in g.neighbors(currentNode):
            if not visitedNodes[node]:
                visitedNodes[node] = True
                waitingNodes.append(node)
                path.append(currentNode)
                break
    return path


if __name__ == '__main__':
    graph = nx.Graph()
    graph.add_nodes_from("ABCDEFG")
    graph.add_edges_from([
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('B', 'E'),
        ('C', 'F'),
        ('E', 'G'),
    ])
    print(dfs(graph, 'A'))

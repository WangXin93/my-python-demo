"""
There are at least 3 represtation for graph: adjacency matrix, list of edges, adjacency list

There complexity of difference represenetaion is:

| idea        | addEdge(s, t) | for(e:adj(v) | printGraph() | hasEdge(s, t) | space used |
|-------------+---------------+--------------+--------------+---------------+------------|
| adjMatrix   | O(1)          | O(V)         | O(V^2)       | O(1)          | O(V^2)     |
| listOfEdges | O(1)          | O(E)         | O(E)         | O(E)          | O(E)       |
| adjList     | O(1)          | O(V)         | O(V+E)       | O(V)          | O(V+E)     |

Default here use adjacent list for graph representation:

graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
"""

from collections import defaultdict
import numpy as np

def adj_list_to_adj_mat(g):
    count = len(g)
    adj = np.zeros((count, count))
    for r, (source, targets) in enumerate(g.items()):
        for c, target in enumerate(targets):
            adj[r][c] = 1
    return adj

def adj_list_to_list_edges(g):
    out = []
    for source, targets in g.items():
        for target in targets:
            out.append((source, target))
    return out

def graph_from_file(filename):
    g = defaultdict(set)
    f = open(filename)
    line = next(f).strip()
    for label in line.split(', '):
        g[label] = set()
    for line in f:
        pred, succ = line.strip().split(', ')
        g[pred].add(succ)
        g[succ].add(pred)
    f.close()
    return g


def weighted_graph_from_file(filename):
    g = defaultdict(set)
    f = open(filename)
    w = dict()
    line = next(f).strip()
    for label in line.split(', '):
        g[label] = set()
    for line in f:
        pred, succ, weight = line.strip().split(', ')
        g[pred].add(succ)
        g[succ].add(pred)
        w[(pred, succ)] = weight
        w[(succ, pred)] = weight
    f.close()
    return g, w


def digraph_from_file(filename):
    g = defaultdict(set)
    f = open(filename)
    line = next(f).strip()
    for label in line.split(', '):
        g[label] = set()
    for line in f:
        pred, succ = line.strip().split(', ')
        g[pred].add(succ)
    f.close()
    return g


def weighted_digraph_from_file(filename):
    g = defaultdict(set)
    w = dict()
    f = open(filename)
    line = next(f).strip()
    for label in line.split(', '):
        g[label] = set()
    for line in f:
        pred, succ, weight = line.strip().split(', ')
        g[pred].add(succ)
        w[(pred, succ)] = int(weight)
    f.close()
    return g, w


if __name__ == "__main__":
    g = graph_from_file("input/sample1.txt")
    print(g)
    print(adj_list_to_adj_mat(g))
    print(adj_list_to_list_edges(g))

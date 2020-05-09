"""
Kruskal’s Algorithm to find minimum spanning tree

Sort all weighted edges and add them if there is no cycle. Repeat add up to V-1 edges.

<https://sp19.datastructur.es/materials/discussion/disc10.pdf>
"""

from unionfind import UnionFind
from graph import weighted_graph_from_file


def kruskal(g, w):
    uf = UnionFind(g.keys())
    w = sorted(w, key=lambda x: w[x])
    edges = list()
    for edge in w:
        a, b = edge
        if not uf.connected(a, b):
            uf.union(a, b)
            edges.append(edge)
        if len(edges) == len(g) - 1:
            break
    return edges


if __name__ == "__main__":
    g, w = weighted_graph_from_file('input/alpha3.txt')
    for key in list(w.keys()):
        if key[0] > key[1]:
            w.pop(key)
    edges = kruskal(g, w)

"""
Prim’s Algorithm to find minimum spanning tree

Each step add a node with minimum weight into a growing tree

Steps:
1. Start from some arbitrary start node.
2. Repeatedly add the shortest edge that has one node inside the MST under construction.
3. Repeat until there are V-1 edges.

<https://sp19.datastructur.es/materials/discussion/disc10.pdf>
"""

from graph import weighted_graph_from_file
from heapq import heappush, heappop
from unionfind import UnionFind


def prim(g, w, start):
    edges = list()
    uf = UnionFind(g.keys())
    q = list()

    for child in g[start]:
        heappush(q, [w[(start, child)], (start, child)])

    while len(edges) < len(g) - 1:
        weight, (a, b) = heappop(q)
        if not uf.connected(a, b):
            edges.append((a, b))
            uf.union(a, b)
            for child in g[b]:
                if child != a:
                    heappush(q, [w[(b, child)], (b, child)])

    return edges


if __name__ == "__main__":
    g, w = weighted_graph_from_file('input/alpha3.txt')
    edges = prim(g, w, start='A')

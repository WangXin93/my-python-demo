"""
A* Algorithm, similar to dijkstra algorithm, use the logic "best first search".

Given a weighted graph ``g`` and start node ``start``, end node 'end':
Set priority queue ``q``, distance table ``dists``, the parent node of a node ``parents``.
Steps:
1. Relax all node except start node value to infinity, push all nodes to priority queue and distance table.
2. Push start node to queue with value 0 and distance 0.
3. While arrive the end node, pop the head of the queue. for each child of current node, if dist(child, current) + dist(current, start) < dist(child, start), update the distance table, update the priority queue with priority value dist(child, current) + dist(current, start) + htable(child)
"""
from graph import weighted_digraph_from_file
from heapq import heappush, heappop, heapify


def a_star(g, start, end, weights, htable):
    q = list()
    dists = dict()
    parents = dict()

    for node in g:
        if node == start:
            heappush(q, [0, start])
            dists[start] = 0
            parents[start] = None
        else:
            heappush(q, [float('inf'), node])
            dists[node] = float('inf')
            parents[node] = None

    while q:
        priority, curr = heappop(q)
        if curr == end:
            break
        for child in g[curr]:
            q_contains_child = any(child == x[1] for x in q)
            if q_contains_child:
                new_dist = dists[curr] + weights[(curr, child)]
                if new_dist < dists[child]:
                    dists[child] = new_dist
                    parents[child] = curr
                    for i, x in enumerate(q):
                        if x[1] == child:
                            q[i][0] = new_dist + htable[child]
                            heapify(q)

    return dists, parents


if __name__ == "__main__":
    g, w = weighted_digraph_from_file('input/alpha2.txt')
    h = {"A": 8, "B": 6, "C": 5, "F": 1, "D": 6, "E": 3, "G": 0}
    dists, parents = a_star(g, 'A', 'G', w, h)

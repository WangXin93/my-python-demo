"""
Dijstra Algorithm, use the logic "best first search".

It can find the shortest path on a weighted graph with non-negative value.

Given a weighted graph ``g`` and start node ``start``:
Set priority queue ``q``, distance table ``dists``, the parent node of a node ``parents``.
Steps:
1. Relax all node except start node value to infinity, push all nodes to priority queue and distance table.
2. Push start node to queue with value 0 and distance 0.
3. While q is not empty, repeat do: pop the head of the queue. for each child of current node, if dist(child, current) + dist(current, start) < dist(child, start), update the distance table, update the priority queue.
"""
from graph import weighted_digraph_from_file
from heapq import heappush, heappop, heapify


def dijkstra(g, start, weights):
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
        for child in g[curr]:
            q_contains_child = any(child == x[1] for x in q)
            if q_contains_child:
                new_dist = dists[curr] + weights[(curr, child)]
                if new_dist < dists[child]:
                    dists[child] = new_dist
                    parents[child] = curr
                    for i, x in enumerate(q):
                        if x[1] == child:
                            q[i][0] = new_dist
                            heapify(q)

    return dists, parents


if __name__ == "__main__":
    g, w = weighted_digraph_from_file('input/alpha2.txt')
    dists, parents = dijkstra(g, 'A', w)

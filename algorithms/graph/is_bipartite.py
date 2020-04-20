"""
https://www.geeksforgeeks.org/bipartite-graph/

Steps:

1. Assign RED color to the source vertex (putting into set U).
2. Color all the neighbors with BLUE color (putting into set V).
3. Color all neighbor’s neighbor with RED color (putting into set U).
4. This way, assign color to all vertices such that it satisfies all the
  constraints of m way coloring problem where m = 2.
5. While assigning colors, if we find a neighbor which is colored with same
  color as current vertex, then the graph cannot be colored with 2 vertices
  (or graph is not Bipartite)
"""

from graph import graph_from_file


def is_bipartite(g, backend="bfs"):
    if backend == "bfs":
        return is_bipartite_dfs(g)
    elif backend == "dfs":
        return is_bipartite_bfs(g)


def is_bipartite_bfs(g):
    q = list()
    colors = {}

    for label in g.keys():
        if label not in colors:
            source = (label, True)
            q.append(source)
            while q:
                label, color = q.pop()
                if label in colors and color != colors[label]:
                    return False
                elif label not in colors:
                    colors[label] = color
                    neighbors = g[label]
                    for neighbor in neighbors:
                        q.append((neighbor, not color))

    return True


def is_bipartite_dfs(g):
    colors = {}
    for label in g.keys():
        if label not in colors:
            if not is_bipartite_dfs_helper(g, label, True, colors):
                return False
    return True


def is_bipartite_dfs_helper(g, label, color, colors):
    if label in colors:
        if colors[label] != color:
            return False
    else:
        colors[label] = color
        neighbors = g[label]
        for neighbor in neighbors:
            if not is_bipartite_dfs_helper(g, neighbor, not color, colors):
                return False
    return True


if __name__ == "__main__":
    print(is_bipartite_bfs(graph_from_file("input/sample1.txt")))
    print(is_bipartite_bfs(graph_from_file("input/sample2.txt")))
    print(is_bipartite_bfs(graph_from_file("input/sample3.txt")))
    print(is_bipartite_bfs(graph_from_file("input/sample4.txt")))

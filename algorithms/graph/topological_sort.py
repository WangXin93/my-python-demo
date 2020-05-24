"""
Topological sort

* Kahn algorithm
* DFS postorder

"""

from graph import digraph_from_file


def dfs(g):
    marked = set()
    stack = []

    def dfs_postorder(node):
        marked.add(node)
        for child in g[node]:
            if child not in marked:
                dfs_postorder(child)
        stack.insert(0, node)

    # Find all source node without income connection
    no_income_sources = set(g)
    for source, targets in g.items():
        for target in targets:
            if target in no_income_sources:
                no_income_sources.remove(target)

    # Post order DFS
    # for node in no_income_sources:
    for node in ["G", "A"]:
        dfs_postorder(node)

    return stack


def kahn(g):
    """ Kahn algorithm.

    Step1: initial all nodes with its in-degree
    Step2: pick all nodew with 0 in-degree, add them to a queue
    Step3: remove a node from the queue then:
        1. increment count of visited nodes by 1
        2. decrease in-degree by 1 for all its neighboring nodes
        3. if in-degree of a neighboring nodes is reduced to zero, add it to the queue
    Step4: repeat step 3 until queue is empty
    Step5: if count of visited nodes is not equal to the number of nodes in the graph, it means it is not a DAG (directed acyclic graph), there is not possible a topological for it.
    """
    indegrees = {n: 0 for n in g}
    for source, targets in g.items():
        for target in targets:
            indegrees[target] += 1

    queue = []
    for node in indegrees:
        if indegrees[node] == 0:
            queue.insert(0, node)

    stack = []
    while queue:
        curr = queue.pop(0)
        stack.append(curr)
        for child in g[curr]:
            indegrees[child] -= 1
            if indegrees[child] == 0:
                queue.append(child)

    if len(stack) != len(g):
        return None
    else:
        return stack


if __name__ == "__main__":
    g = digraph_from_file("input/alpha1.txt")
    print(dfs(g))
    print(kahn(g))

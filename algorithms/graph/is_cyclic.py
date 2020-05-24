""" Compute whether a graph has cycle.
"""
from graph import digraph_from_file


def dfs(g):
    marked = set()

    def dfs_preorder(node):
        print("{}, {}".format(node, marked))
        if node in marked:
            return False
        marked.add(node)
        for child in g[node]:
            if not dfs_preorder(child):
                return False
        marked.remove(node)
        return True

    noincome_sources = set(g)
    for source, targets in g.items():
        for target in targets:
            if target in noincome_sources:
                noincome_sources.remove(target)

    for source in noincome_sources:
        if not dfs_preorder(source):
            return False
    return True


if __name__ == "__main__":
    g = digraph_from_file("input/alpha1.txt")
    print(dfs(g))

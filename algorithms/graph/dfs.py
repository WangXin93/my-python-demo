from graph import digraph_from_file


def dfs(g):
    marked = set()

    def dfs_preorder(node):
        print(node)
        for child in g[node]:
            if child not in marked:
                marked.add(child)
                dfs_preorder(child)

    def dfs_postorder(node):
        for child in g[node]:
            if child not in marked:
                marked.add(child)
                dfs_postorder(child)
        print(node)

    for node in g.keys():
        if node not in marked:
            # dfs_preorder(node)
            dfs_postorder(node)


if __name__ == "__main__":
    g = digraph_from_file("input/alpha1.txt")
    dfs(g)

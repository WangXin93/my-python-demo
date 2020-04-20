from graph import *
from is_bipartite import *

def test_input1():
    g = graph_from_file("input/sample1.txt")
    assert is_bipartite_dfs(g) is True
    assert is_bipartite_bfs(g) is True

def test_input2():
    g = graph_from_file("input/sample2.txt")
    assert is_bipartite_dfs(g) is True
    assert is_bipartite_bfs(g) is True

def test_input3():
    g = graph_from_file("input/sample3.txt")
    assert is_bipartite_dfs(g) is False
    assert is_bipartite_bfs(g) is False

def test_input4():
    g = graph_from_file("input/sample4.txt")
    assert is_bipartite_dfs(g) is False
    assert is_bipartite_bfs(g) is False

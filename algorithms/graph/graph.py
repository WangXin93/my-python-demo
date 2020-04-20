"""
graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
"""

from collections import defaultdict

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

if __name__ == "__main__":
    g = graph_from_file("input/sample1.txt")
    print(g)

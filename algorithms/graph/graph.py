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


def weighted_graph_from_file(filename):
    g = defaultdict(set)
    f = open(filename)
    w = dict()
    line = next(f).strip()
    for label in line.split(', '):
        g[label] = set()
    for line in f:
        pred, succ, weight = line.strip().split(', ')
        g[pred].add(succ)
        g[succ].add(pred)
        w[(pred, succ)] = weight
        w[(succ, pred)] = weight
    f.close()
    return g, w


def digraph_from_file(filename):
    g = defaultdict(set)
    f = open(filename)
    line = next(f).strip()
    for label in line.split(', '):
        g[label] = set()
    for line in f:
        pred, succ = line.strip().split(', ')
        g[pred].add(succ)
    f.close()
    return g


def weighted_digraph_from_file(filename):
    g = defaultdict(set)
    w = dict()
    f = open(filename)
    line = next(f).strip()
    for label in line.split(', '):
        g[label] = set()
    for line in f:
        pred, succ, weight = line.strip().split(', ')
        g[pred].add(succ)
        w[(pred, succ)] = int(weight)
    f.close()
    return g, w


if __name__ == "__main__":
    g = graph_from_file("input/sample1.txt")
    print(g)

"""
Dijkestra算法适合有向无环图（directed acyclic graph),对于有负权边的图使用
Bellman ford algorithm.

graph:

start ---5-->A--4-->D--3
   \         ^\     |   \
    \        | \    |    >
     \       8  2   6   final 
      \      |   \  |    > 
       \     |    > v   /
        \-2->B--7-->C--1
"""
graph = {}
graph['start'] = {}
graph['start']['A'] = 5
graph['start']['B'] = 2
graph['A'] = {}
graph['A']['D'] = 4
graph['A']['C'] = 2
graph['B'] = {}
graph['B']['C'] = 7
graph['C'] = {}
graph['C']['final'] = 1
graph['D'] = {}
graph['D']['C'] = 6
graph['D']['final'] = 3
graph['final'] = {}

infinity = float("inf")
costs = {}
costs['A'] = 5
costs['B'] = 2
costs['C'] = infinity
costs['D'] = infinity
costs['final'] = infinity

parents = {}
parents['A'] = 'start'
parents['B'] = 'start'
parents['C'] = None
parents['D'] = None
parents['final'] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def main():
    while True:
        node = find_lowest_cost_node(costs)
        if not node:
            break
        cost = costs[node]
        neightbors = graph[node]
        for n in neightbors.keys():
            new_cost = cost + neightbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)

    print("COSTS: ")
    print(costs)
    print("PARENTS: ")
    print(parents)
    print("The shortest way is: (COST: %s)" % costs['final'])
    shortest_way = 'final'
    point = 'final'
    while True:
        shortest_way += " --> %s" % parents[point]
        if parents[point] == 'start':
            break
        else:
            point = parents[point]
    print(shortest_way)

if __name__ == "__main__":
    main()

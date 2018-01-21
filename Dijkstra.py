graph = {}
costs = {}
parents = {}
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

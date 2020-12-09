# the graph
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# print("graph dictionary is as follows: ", graph)

# the costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# print("the costs dictionary is as follows: ", costs)

# the parents table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

# print("the parents dictionary is as follows: ", parents)

processed = []


def find_lowest_cost_node(costs_dict):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Go through each node.
    for _node in costs_dict:
        _cost = costs_dict[_node]
        # If it's the lowest cost so far and hasn't been processed yet...
        if _cost < lowest_cost and _node not in processed:
            # ... set it as the new lowest-cost node.
            lowest_cost = _cost
            lowest_cost_node = _node
    return lowest_cost_node


# Find the lowest-cost node that you haven't processed yet.
node = find_lowest_cost_node(costs)
# If you've processed all the nodes, this while loop is done.
while node is not None:
    cost = costs[node]
    # Go through all the neighbors of this node.
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # If it's cheaper to get to this neighbor by going through this node...
        if costs[n] > new_cost:
            # ... update the cost for this node.
            costs[n] = new_cost
            # This node becomes the new parent for this neighbor.
            parents[n] = node
    # Mark the node as processed.
    processed.append(node)
    # Find the next node to process, and loop.
    node = find_lowest_cost_node(costs)

print("Cost from the start to each node:")
print(costs)

# print("parents dictionary is now as follows: ", parents)

path = []

step = "fin"

while step != "start":
    path.append(parents[step])
    step = parents[step]

print("the fastest path is as follows: ", end="")
print(*list(reversed(path)), sep=" --> ")

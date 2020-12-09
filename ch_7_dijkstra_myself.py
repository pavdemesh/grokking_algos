# the graph
graph_dict = {}
graph_dict["start"] = {}
graph_dict["start"]["a"] = 6
graph_dict["start"]["b"] = 2

graph_dict["a"] = {}
graph_dict["a"]["fin"] = 1

graph_dict["b"] = {}
graph_dict["b"]["a"] = 3
graph_dict["b"]["fin"] = 5

graph_dict["fin"] = {}

# print("graph dictionary is as follows: ", graph)

# the costs table
infinity = float("inf")
costs_dict = {}
costs_dict["a"] = 6
costs_dict["b"] = 2
costs_dict["fin"] = infinity

# print("the costs dictionary is as follows: ", costs)

# the parents table
parents_dict = {}
parents_dict["a"] = "start"
parents_dict["b"] = "start"
parents_dict["fin"] = None

# print("the parents dictionary is as follows: ", parents)

# A list to keep track of already processed nodes
processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None

    for node in costs.keys():
        if node not in processed and costs[node] < lowest_cost:
            lowest_cost = costs[node]
            lowest_cost_node = node

    return lowest_cost_node


# print(find_lowest_cost_node(costs_dict))

def dijkstra_algo(graph, costs, parents):
    current_node = find_lowest_cost_node(costs)

    while current_node is not None:
        for neighbor in graph[current_node].keys():
            new_cost = costs[current_node] + graph[current_node][neighbor]
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                parents[neighbor] = current_node
        processed.append(current_node)
        current_node = find_lowest_cost_node(costs)

    return parents


dijkstra_algo(graph_dict, costs_dict, parents_dict)

path = []
step = "fin"

while step != "start":
    path.append(step)
    step = parents_dict[step]

path.append("start")

print(*reversed(path), sep=" --> ")

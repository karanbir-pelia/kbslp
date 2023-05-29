
import heapq


def a_star(start, goal, graph):

    open_list = [(0, start)]
    closed_list = set()

    path = {start: None}
    cost = {start: 0}

    while open_list:

        current_cost, current_node = heapq.heappop(open_list)

        closed_list.add(current_node)

        if current_node == goal:
            return reconstruct_path(path, start, goal)

        for neighbor, weight in graph[current_node].items():

            tentative_cost = cost[current_node] + weight

            if neighbor in closed_list:
                continue

            if neighbor not in [node for _, node in open_list] or tentative_cost < cost[neighbor]:

                path[neighbor] = current_node
                cost[neighbor] = tentative_cost

                heuristic_value = heuristic(neighbor, goal)

                heapq.heappush(open_list, (tentative_cost +
                               heuristic_value, neighbor))

    return None


def reconstruct_path(path, start, goal):

    current_node = goal
    path_nodes = []

    while current_node != start:
        path_nodes.append(current_node)
        current_node = path[current_node]

    path_nodes.append(start)

    path_nodes.reverse()

    return path_nodes


def heuristic(node, goal):
    return abs(ord(node) - ord(goal))


def get_graph_from_user():
    graph = {}

    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        source = input("Enter the source node: ")
        target = input("Enter the target node: ")
        weight = int(input("Enter the weight: "))

        if source not in graph:
            graph[source] = {}
        graph[source][target] = weight

    return graph


graph = get_graph_from_user()

start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")
shortest_path = a_star(start_node, goal_node, graph)

if shortest_path is None:
    print("No path found.")
else:
    print("Shortest path:", ' -> '.join(shortest_path))


def graph_coloring(graph, num_colors):
    colors = [0] * len(graph)

    def is_safe(vertex, color):
        for neighbor in graph[vertex]:
            if colors[neighbor] == color:
                return False
        return True

    def backtrack(vertex):
        if vertex == len(graph):
            return True

        for color in range(1, num_colors + 1):
            if is_safe(vertex, color):
                colors[vertex] = color

                if backtrack(vertex + 1):
                    return True

                colors[vertex] = 0

        return False

    if backtrack(0):
        print("Color assignment:")
        for vertex, color in enumerate(colors):
            print(f"Vertex {vertex}: Color {color}")
    else:
        print("No solution found.")


num_vertices = int(input("Enter the number of vertices: "))

graph = {}
for vertex in range(num_vertices):
    neighbors = input(
        f"Enter the neighbors of vertex {vertex} (separated by spaces): ").split()
    graph[vertex] = [int(neighbor) for neighbor in neighbors]

num_colors = int(input("Enter the number of colors: "))

graph_coloring(graph, num_colors)

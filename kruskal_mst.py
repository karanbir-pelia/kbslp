class Graph:
    def __init__(self, number_of_vertices: int) -> None:
        self.number_of_vertices = number_of_vertices
        self.graph = []

    def add_edge(self, start, end, weight: int):
        self.graph.append((start, end, weight))

    def find_parent(self, parent: list, node):
        if parent[node] != node:
            parent[node] = self.find_parent(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, node_1, node_2):
        if rank[node_1] > rank[node_2]:
            parent[node_2] = node_1
        elif rank[node_2] > rank[node_1]:
            parent[node_1] = node_2
        else:
            parent[node_2] = node_1
            rank[node_1] += 1

    def Kruskals_MST(self):
        result = []

        current_index = 0
        edges_added = 0

        self.graph = sorted(self.graph, key=lambda edge: edge[2])

        parent = []
        rank = []

        for node in range(self.number_of_vertices):
            parent.append(node)
            rank.append(0)

        while edges_added < self.number_of_vertices - 1:
            start, end, weight = self.graph[current_index]
            current_index += 1
            parent_start = self.find_parent(parent, start)
            parent_end = self.find_parent(parent, end)

            if parent_start != parent_end:
                edges_added += 1
                result.append([start, end, weight])
                self.union(parent, rank, start, end)

        minimum_cost = 0

        print("\n Edge      Weight\n")
        for start, end, weight in result:
            minimum_cost += weight
            print(f"{start} --- {end}      {weight}")

        print(f"\nThe minimum cost is {minimum_cost}.\n")


if __name__ == "__main__":
    graph = Graph(6)
    graph.add_edge(0, 1, 4)
    graph.add_edge(1, 2, 9)
    graph.add_edge(2, 3, 2)
    graph.add_edge(3, 4, 6)
    graph.add_edge(4, 5, 1)
    graph.add_edge(5, 0, 8)
    graph.add_edge(1, 5, 11)
    graph.add_edge(3, 5, 7)

    graph.Kruskals_MST()

from random import choice


class Graph:
    def __init__(self, number_of_vertices: int) -> None:
        self.number_of_vertices = number_of_vertices
        self.graph = {i: [] for i in range(self.number_of_vertices)}
        self.parent = {i: None for i in range(self.number_of_vertices)}
        self.distance = {i: float("inf")
                         for i in range(self.number_of_vertices)}
        self.visited = {i: False for i in range(self.number_of_vertices)}

    def add_edge(self, start, end, weight: int):
        self.graph[start].append((end, weight))
        self.graph[end].append((start, weight))

    def Prims_MST(self):
        start = choice(list(self.graph.keys()))

        bag = []
        self.distance[start] = 0
        self.parent[start] = -1
        bag.append((start, 0))

        while bag:
            current_node, current_weight = bag.pop(0)
            self.visited[current_node] = True
            for node, weight in self.graph[current_node]:
                if not self.visited[node] and weight < self.distance[node]:
                    self.distance[node] = weight
                    self.parent[node] = current_node
                    bag.append((node, weight))
                    bag = sorted(bag, key=lambda node: node[1])

        print("\n Edge      Weight\n")
        for node in range(self.number_of_vertices):
            if node != start:
                print(
                    f"{self.parent[node]} --- {node}      {self.distance[node]}")
        print(f"\nThe minimum cost is {sum(self.distance.values())}.\n")


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

    graph.Prims_MST()

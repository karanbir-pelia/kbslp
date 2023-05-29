
from random import choice


class Queue:
    def __init__(self) -> None:
        self.elements = []

    def insert(self, element):
        self.elements.append(element)

    def pop(self):
        return self.elements.pop(0)

    def peek(self):
        return self.elements[0]

    def is_empty(self):
        return not bool(len(self.elements))


def bfs(graph: dict):
    queue = Queue()

    queue.insert(choice(list(graph.keys())))

    visited = [queue.peek()]

    while not queue.is_empty():
        node = queue.pop()

        for element in graph[node]:
            if element not in visited:
                queue.insert(element)
                visited.append(element)

    return visited


def dfs(graph: dict, root):

    for node in graph[root]:
        if node not in visited:
            visited.append(node)
            dfs(graph, node)

    return visited


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D", "E"],
    "D": ["B", "C", "E"],
    "E": ["C", "D"]
}

visited = [choice(list(graph.keys()))]

print('''
Graph:
            A ------ C
            |      / | \\
            |     /  |  \\
            |    /   |   \\
            |   /    |    E
            |  /     |  /
            | /      | /
            B ------ D
      ''')

print(f"BFS : {bfs(graph)}")
print(f"DFS : {dfs(graph, visited[0])}")

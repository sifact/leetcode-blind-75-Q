"""
class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print(self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph_dict:
            return []

        paths = []

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths

    def get_shortest_path(self, start, end, path=[]):

        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None

        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path


routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]

route_graph = Graph(routes)

starts = "Mumbai"
ends = "Toronto"

print(f"Path between {starts} and {ends} {route_graph.get_path(starts, ends)}")
print(f"Shortest path between {starts} and {ends} {route_graph.get_shortest_path(starts, ends)}")

"""


import math
def divide_str(s):

    n = len(s)

    i = 0
    while n > 0:
        n = math.floor(n / 2)

        print(s[i:n])
        s = s[n: len(s)]


string = "I am in the exam hall"
divide_str(string)





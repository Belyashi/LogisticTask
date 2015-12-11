from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance


def dijsktra(graph, initial, destination):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[(min_node, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    result = []
    while destination != initial:
        result.append(destination)
        destination = path[destination]
    result.append(initial)
    result.reverse()
    return result


if __name__ == '__main__':

    g = Graph()
    for i in xrange(1, 11):
        g.add_node(i)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 11)
    g.add_edge(1, 4, 11)
    g.add_edge(1, 5, 11)
    g.add_edge(2, 7, 10)
    g.add_edge(3, 8, 50)
    g.add_edge(4, 6, 6)
    g.add_edge(4, 10, 15)
    g.add_edge(5, 9, 12)
    g.add_edge(6, 9, 7)
    g.add_edge(7, 8, 20)
    g.add_edge(9, 10, 1)
    g.add_edge(10, 8, 6)

    start, end = 1, 8
    print dijsktra(g, start, end)

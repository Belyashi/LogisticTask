from collections import defaultdict

from map import Map


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance


def dijsktra(initial, destination):
    graph = __make_graph()
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


def __make_graph():
    if hasattr(__make_graph, 'graph'):
        return __make_graph.graph
    graph = Graph()
    mp = Map()
    ways = mp.get_all_ways()
    for way in ways:
        start_city_id = way['start_city_id']
        finish_city_id = way['finish_city_id']
        length = way['length']
        graph.add_node(start_city_id)
        graph.add_node(finish_city_id)
        graph.add_edge(start_city_id, finish_city_id, length)
    setattr(__make_graph, 'graph', graph)
    return __make_graph.graph

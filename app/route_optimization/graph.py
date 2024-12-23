import networkx as nx

def create_graph(edges):
    graph = nx.Graph()
    graph.add_weighted_edges_from(edges)
    return graph

def get_shortest_path(graph, source, target):
    path = nx.shortest_path(graph, source=source, target=target, weight='weight')
    distance = nx.shortest_path_length(graph, source=source, target=target, weight='weight')
    return path, distance

from JsonFuncs import *

# load_graph_from_json
json_WeightedGraph = load_graph_from_json('weighted_graph.json')

# get_vertices
print('Graph vertices: {}'.format(json_WeightedGraph.get_vertices()))

# get_edges
print('\nGraph edges: {}'.format(json_WeightedGraph.get_edges()))

# add_vertex
json_WeightedGraph.add_vertex('Herzliya', [['Haifa', 5.62]])
print('\nAdd to graph: "Herzliya":[["Haifa",5.62]]')

# delete_vertex
json_WeightedGraph.delete_vertex('Tel-Aviv')
print('\nDeleted from graph: "Tel-Aviv"')

# BFS
print('\nThe paths from "Holon" to "Bat-Yam": {}'.format(json_WeightedGraph.BFS("Holon", "Bat-Yam")))

# get_shortest_path
print('\nThe shortest paths from "Holon" to "Bat-Yam": {}'.format(
    json_WeightedGraph.get_shortest_path("Holon", "Bat-Yam")))

# serialize
serialized_graph=json_WeightedGraph.serialize()
print(serialized_graph)

# deserialize
deserialize_graph=WeightedGraph.deserialize(serialized_graph)

# save_graph_to_json
save_graph_to_json(json_WeightedGraph, 'new_weighted_graph.json')
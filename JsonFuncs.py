import json
from WeightedGraph import *


def load_graph_from_json(file_name):
    if file_name.find('.json') == -1:
        str = '.json'
        file_name += str
    try:
        with open(file_name, 'r') as file:
            json_file_data = json.load(file)
        json_graph = WeightedGraph(json_file_data)
    except:
        print('Error while handling file:', file_name)
        return
    return json_graph


def save_graph_to_json(graph, file_name):
    if file_name.find('.json') == -1:
        file_name += '.json'
    try:
        with open(file_name, 'w') as file:
            json.dump(graph.serialize(), file)
    except:
        print('Error while handling file:', file_name)
        return
    return

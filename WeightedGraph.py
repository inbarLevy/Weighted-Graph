from collections import deque
import math


def validate_weight(weight):
    if isinstance(weight, (int, float)) and not isinstance(weight, bool):
        return bool(weight >= 0)
    return False


def validate_type(dict):
    return type(list(dict.keys())[0])


class WeightedGraph:
    def __init__(self, dict):
        self.v_type = validate_type(dict)
        self.hashTable = WeightedGraph.deserialize(dict)

    @staticmethod
    def deserialize(dict):
        weightedgraph = {}
        try:
            for vertex in dict:
                if type(vertex) == type(list(dict.keys())[0]):
                    if vertex not in weightedgraph:
                        weightedgraph[vertex] = {}
                    for connection in dict[vertex]:
                        if validate_weight(connection[1]):
                            if connection[0] == vertex:
                                print("Can't connect vertex to itself. Not added to graph: {vertex:" + str(
                                    connection[0]) + ', vertex:' + str(vertex) +
                                      ', weight:' + str(connection[1]) + '}')
                            elif connection[0] not in weightedgraph:
                                weightedgraph[connection[0]] = {}
                            weightedgraph[vertex][connection[0]] = connection[1]
                            weightedgraph[connection[0]][vertex] = connection[1]
                        else:
                            print('weight is not a number. Not added to graph: {vertex:' + str(
                                connection[0]) + ', vertex:' + str(vertex) + ', weight:' + str(
                                connection[1]) + '}')
                else:
                    print('incorrect vertex value. Not added to graph: vertex-' + vertex)
        except:
            print('Error with input value')
        finally:
            return weightedgraph

    def get_vertices(self):
        return list(self.hashTable)

    def get_edges(self):
        edges = []
        for source in self.hashTable:
            for target in self.hashTable[source]:
                if (source, target, self.hashTable[source][target]) not in edges and (
                        target, source, self.hashTable[source][target]) not in edges:
                    edges.append((source, target, self.hashTable[source][target]))
        return edges

    def add_vertex(self, vertex, connections):
        try:
            if type(vertex) == self.v_type or len(connections) != 0:
                if vertex not in self.hashTable:
                    self.hashTable[vertex] = {}
                for connection in connections:
                    if validate_weight(connection[1]):
                        if connection[0] == vertex:
                            print("Can't connect vertex to itself. Not added to graph: {vertex:" + str(
                                connection[0]) + ', vertex:' + str(vertex) +
                                  ', weight:' + str(connection[1]) + '}')
                        elif connection[0] not in self.hashTable:
                            print('Vertex ' + str(connection[0]) + ' is not in the graph. ' +
                                  'Not added to graph: {vertex:' + str(connection[0]) + ', vertex:' +
                                  str(vertex) + ', weight:' + str(connection[1]) + '}')
                        elif vertex not in self.hashTable[connection[0]] or \
                                connection[0] not in self.hashTable[vertex]:
                            self.hashTable[vertex][connection[0]] = connection[1]
                            self.hashTable[connection[0]][vertex] = connection[1]
                        else:
                            print('Vertices are already connected. Not added to graph: {vertex:' + str(
                                connection[0]) + ', vertex:' + str(vertex) + ', weight:' + str(
                                connection[1]) + '}')
                    else:
                        print('weight is not a number. Not added to graph: {vertex:' + str(
                            connection[0]) + ', vertex:' + str(vertex) + ', weight:' + str(connection[1]) + '}')
            else:
                print('incorrect input values')
        except:
            print('incorrect input values')

    def delete_vertex(self, unwanted_vertex):
        try:
            if type(unwanted_vertex) == self.v_type:
                if unwanted_vertex not in self.hashTable:
                    print('Vertex does not exist in graph')
                else:
                    del self.hashTable[unwanted_vertex]
                    for vertex in self.hashTable:
                        if unwanted_vertex in self.hashTable[vertex]:
                            del self.hashTable[vertex][unwanted_vertex]
            else:
                print('incorrect input values')
        except:
            print('incorrect input values')

    def find_paths(self, start, goal):
        try:
            if type(start) == self.v_type and type(goal) == self.v_type:
                min_weight = math.inf
                queue = deque()
                queue.append((start, [start], 0))
                all_path_results = []
                shortest_path_result = []
                while queue:
                    (vertex, path, weight) = queue.popleft()
                    for next in set(self.hashTable[vertex]) - set(path):
                        if next == goal:
                            all_path_results.append(path + [next])
                            if weight + self.hashTable[vertex][next] < min_weight:
                                shortest_path_result = path + [next]
                                min_weight = weight + self.hashTable[vertex][next]
                            elif weight + self.hashTable[vertex][next] == min_weight:
                                shortest_path_result.append(path + [next])
                        else:
                            queue.append((next, path + [next], weight + self.hashTable[vertex][next]))
                return all_path_results, shortest_path_result
            else:
                print('incorrect input values')
        except:
            print('incorrect input values')

    def BFS(self, start, goal):
        (all_path, shortest_path) = self.find_paths(start, goal)
        return all_path

    def get_shortest_path(self, start, goal):
        (all_path, shortest_path) = self.find_paths(start, goal)
        return shortest_path

    def serialize(self):
        hash_table = {}
        for vertex in self.hashTable:
            hash_table[vertex] = []
            for next in self.hashTable[vertex]:
                hash_table[vertex].append([next, self.hashTable[vertex][next]])
        return hash_table

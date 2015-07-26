# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
# major help from http://www.ics.uci.edu/~eppstein/161/python/dijkstra.py


class Graph(object):
    """
    Respresents a graph as a dictionarty of nodes.
    """
    def __init__(self):
        self.graph = {}

    def nodes(self):
        """
        Returns a list of nodes in graph.
        """
        return self.graph.keys()

    def edges(self):
        """
        Returns a list of all edges in graph.
        """
        edges = []
        for key, values in self.graph.iteritems():
            for node in values:
                    edges.append((key, node))
        return edges

    def add_node(self, node):
        """
        Adds a node to the Graph.
        """
        self.graph[node] = []

    def add_edge(self, node1, node2, weight=0):
        """
        Creats an edge between two nodes with a weight.
        """
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        self.graph[node1].append((node2, weight))

    def del_node(self, node):
        """
        Delete an existing node from the Graph
        """
        try:
            del self.graph[node]
            for nodes in self.graph.iterkeys():
                if node in self.graph[nodes]:
                    self.graph[nodes].remove(node)
        except KeyError:
            raise IndexError("Node doesn't exist")

    def del_edge(self, node1, node2):
        """
        Delete an edge from the Graph. If an edge doesn't exist pass
        """
        try:
            for num in range(len(self.graph[node1])):
                if self.graph[node1][num][0] == node2:
                    self.graph[node1].remove(self.graph[node1][num])
                    break
        except ValueError:
            pass
        except KeyError:
            raise IndexError("First node doesn't exist")

    def has_node(self, node):
        """
        Check is node is in graph.
        """
        return node in self.graph

    def neighbors(self, node):
        """
        Finds the adjacent edges for a given node.
        """
        if node in self.graph:
            return self.graph[node]
        else:
            raise KeyError('Node not in graph.')

    def adjacent(self, node1, node2):
        """
        Finds an edge between two nodees
        """
        if node1 not in self.graph or node2 not in self.graph:
            raise IndexError('Node does not exist')
        return node2 in self.graph[node1]

    def depth_first_traversal(self, start):
        """Returns a depth first traversal path as a list.
        """
        visited = []
        begin = [start]

        while begin:
            node = begin.pop(0)
            if node not in visited:
                visited.append(node)
                begin = self.neighbors(node) + begin
        return visited

    def breadth_first_traversal(self, start):
        """Returns a breadth first travesal path as a list.
        """
        visited = []
        begin = [start]

        while begin:
            node = begin.pop(0)
            if node not in visited:
                visited.append(node)
                begin = begin + self.neighbors(node)
        return visited

    def dijkstra(self, start, end):
        """
        Returns shortes path from start to end
        """
        if start == end:
            return [start], 0
        current = start
        path = [start]
        path_weight = 0

        while not current == end:
            weight = float('inf')
            smallest = None
            for node in self.graph[current]:
                if node[1] < weight and node[0] not in path:
                    smallest = node[0]
                    weight = node[1]
            path.append(smallest)
            path_weight += weight
            current = smallest

        return path, path_weight

if __name__ == '__main__':
    x = Graph()

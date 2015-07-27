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
                    edges.append((key, node[0]))
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
        if not self.graph.has_key(node1):
            self.add_node(node1)
        if not self.graph.has_key(node1):
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
        Return the edges for a node in a list
        """
        try:
            edges = [node[0] for node in self.graph[node]]
            return edges
        except KeyError:
            raise IndexError("Node not in Graph.")

    def adjacent(self, node1, node2):
        """
        Return if an edge exist between two nodes
        """
        try:
            return node2 in self.neighbors(node1)
        except KeyError:
            raise IndexError("Node not in Graph.")

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
    x.add_node(1)
    x.add_node(2)
    x.add_node(3)
    x.add_node(4)
    x.add_node(5)
    x.add_node(6)
    x.nodes()
    x.add_edge(1, 2, 10)
    x.add_edge(2, 3, 11)
    x.add_edge(2, 5, 0)
    x.add_edge(5, 6, 1)
    x.add_edge(4, 5, 90)


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from graph_weighted import Graph
<<<<<<< HEAD

def test_bredth_traversal():
=======
import pytest


@pytest.fixture()
def graph1():
>>>>>>> 069081b32ae7c9ea5dced364a81db2af68e4e1b1
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 6)
    g.add_edge(3, 8)
    g.add_edge(4, 9)
    g.add_edge(5, 10)
    g.add_edge(6, 8)
    g.add_edge(7, 9)
    g.add_edge(8, 9)
<<<<<<< HEAD
    assert g.breadth_first_traversal(1) == [1, 2, 5, 3, 6, 10, 8, 9]

def test_depth_traversal():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(1, 2)
    g.add_edge(1, 5)
    g.add_edge(2, 3)
    g.add_edge(2, 6)
    g.add_edge(3, 8)
    g.add_edge(4, 9)
    g.add_edge(5, 10)
    g.add_edge(6, 8)
    g.add_edge(7, 9)
    g.add_edge(8, 9)
=======
    return g


def test_nodes(graph1):
    g = graph1
    assert g.nodes() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_has_node(graph1):
    g = graph1
    assert g.has_node(5) == True


def test_has_edges(graph1):
    g = graph1
    assert g.edges() == [(1, 2), (1, 5), (2, 3), (2, 6), (3, 8), (4, 9), (5, 10), (6, 8), (7, 9), (8, 9)]


def test_neighbors(graph1):
    g = graph1
    assert g.neighbors(5) == [10]


def test_adjacent(graph1):
    g = graph1
    assert g.adjacent(1, 2) == True


def test_bredth_traversal(graph1):
    g = graph1
    assert g.breadth_first_traversal(1) == [1, 2, 5, 3, 6, 10, 8, 9]


def test_depth_traversal(graph1):
    g = graph1
>>>>>>> 069081b32ae7c9ea5dced364a81db2af68e4e1b1
    assert g.depth_first_traversal(1) == [1, 2, 3, 8, 9, 6, 5, 10]


def test_dijkstra():
    g = Graph()
    g.add_node('1')
    g.add_edge('1', '2', 8)
    g.add_edge('1', '5', 4)
    g.add_edge('2', '3', 7)
<<<<<<< HEAD
    g.add_edge('2', 'e', 10)
=======
    g.add_edge('2', '5', 10)
>>>>>>> 069081b32ae7c9ea5dced364a81db2af68e4e1b1
    g.add_edge('3', '4', 5)
    g.add_edge('5', '3', 4)
    g.add_edge('5', '4', 1)
    g.add_edge('5', '6', 2)
    g.add_edge('6', '1', 9)
    assert g.dijkstra('1', '4') == (['1', '5', '4'], 5)

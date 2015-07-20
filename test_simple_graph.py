from simple_graph import SimpleGraph, Node


def make_a_simplegraph():
    nodes = (Node(5), Node("woo"), Node(object()), Node("pikachu"))
    nodes[0].pointers.append(nodes[1])
    nodes[0].pointers.append(nodes[2])
    nodes[1].pointers.append(nodes[2])
    nodes[2].pointers.append(nodes[3])
    nodes[3].pointers.append(nodes[1])
    nodes[3].pointers.append(nodes[0])
    return SimpleGraph(nodes)


def test_nodes():
    g = make_a_simplegraph()
    nodes = g.nodes()
    assert len(nodes) == 4
    assert type(nodes) == list
    for n in nodes:
        assert type(n) == Node


def test_edges():
    g = make_a_simplegraph()
    edges = g.edges()
    assert type(edges) == list
    assert type(edges[0]) == tuple
    for n in g._nodes:
        for n2 in n.pointers:
            assert (n, n2) in edges


def test_add_node():
    g = make_a_simplegraph()
    node = Node("Me!")
    g.add_node(node)
    assert node in g.nodes()


def test_add_edge():
    g = make_a_simplegraph()
    nodes = g.nodes()
    edge = (nodes[0], nodes[3])
    assert edge not in g.edges()
    g.add_edge(edge[0], edge[1])
    assert edge in g.edges()


def test_del_node():
    g = make_a_simplegraph()
    node = g.nodes()[2]
    helper = Node("helper")
    g.add_node(helper)
    g.add_edge(helper, node)
    assert g.has_node(node)
    assert (helper, node) in g.edges()
    g.del_node(node)
    assert not g.has_node(node)
    assert (helper, node) not in g.edges()


def test_del_edge():
    g = make_a_simplegraph()
    node = g.nodes()[2]
    helper = Node("helper")
    g.add_node(helper)
    g.add_edge(helper, node)
    assert (helper, node) in g.edges()
    g.del_edge(helper, node)
    assert (helper, node) not in g.edges()


def test_has_node():
    g = make_a_simplegraph()
    node = g.nodes()[0]
    assert g.has_node(node)
    assert not g.has_node(Node("Nope"))


def test_neighbors():
    g = make_a_simplegraph()
    node = g.nodes()[2]
    helper = Node("helper")
    g.add_node(helper)
    assert node not in g.neighbors(helper)
    g.add_edge(helper, node)
    assert node in g.neighbors(helper)


def test_adjacent():
    g = make_a_simplegraph()
    node = g.nodes()[2]
    helper = Node("helper")
    g.add_node(helper)
    assert not g.adjacent(helper, node)
    g.add_edge(helper, node)
    assert g.adjacent(helper, node)

from bst import BinarySearchTree, Node

def test_balance():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(4)
    tree.insert(5)
    tree.insert(1)
    assert tree.balance() != 0
    assert tree.balance() == 1

def test_depth():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(4)
    tree.insert(5)
    tree.insert(1)
    assert tree.depth() != 2
    assert tree.depth() == 3

def test_size():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(4)
    tree.insert(5)
    tree.insert(1)
    assert tree.size() != 2
    assert tree.size() == 4

def test_contains():
    tree = BinarySearchTree()
    tree.insert(2)
    tree.insert(4)
    tree.insert(5)
    tree.insert(1)
    assert tree.contains(4) == True
    assert tree.contains(10) == False

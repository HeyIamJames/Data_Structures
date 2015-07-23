import pytest
import random
from bst import BinarySearchTree, Node


@pytest.fixture
def empty_bst():
    return BinarySearchTree()


@pytest.fixture
def fixed_six_node_bst():
    tree = BinarySearchTree()
    tree.insert(15)
    tree.insert(7)
    tree.insert(20)
    tree.insert(3)
    tree.insert(9)
    tree.insert(2)
    return tree


# @pytest.fixture
# def random_ten_node_bst():
#     tree = BinarySearchTree()
#     my_set = set()
#     for i in range(10):
#         r = random.randint(1, 50)
#         tree.insert(r)
#         my_set.add(r)
#     return (tree, my_set)


def test_insert_empty_tree(empty_bst):
    my_tree = empty_bst
    my_tree.insert(random.randint(1, 10))
    assert my_tree.root is not None
    assert len(my_tree.set) == 1


def test_insert_duplicate_val(fixed_six_node_bst):
    my_tree = fixed_six_node_bst
    assert len(my_tree.set) == 6
    my_tree.insert(20)
    assert len(my_tree.set) == 6


def test_insert_populated_tree(fixed_six_node_bst):
    my_tree = fixed_six_node_bst
    assert len(my_tree.set) == 6
    my_tree.insert(14)
    assert len(my_tree.set) == 7


def test_insert_positioning(fixed_six_node_bst):
    my_tree = fixed_six_node_bst
    assert my_tree.root.val == 15
    # check right side
    assert my_tree.root.right.val == 20
    assert my_tree.root.right.right is None
    # check left side
    left_1 = my_tree.root.left
    left_2 = left_1.left
    assert left_1.val == 7
    assert left_1.right.val == 9
    assert left_1.right.right is None
    assert left_2.val == 3
    assert left_2.left.val == 2
    assert left_2.left.left is None


def test_contains_empty(empty_bst):
    my_tree = empty_bst
    assert my_tree.contains(10) is False


def test_contains_populated(fixed_six_node_bst):
    my_tree = fixed_six_node_bst
    assert my_tree.contains(9)
    assert my_tree.contains(20)
    assert my_tree.contains(3)
    assert my_tree.contains(8) is False


def test_size_empty(empty_bst):
    my_tree = empty_bst
    assert my_tree.size() == 0


def test_size_populated(fixed_six_node_bst):
    my_tree = fixed_six_node_bst
    assert len(my_tree.set) == 6
    assert my_tree.size() == 6


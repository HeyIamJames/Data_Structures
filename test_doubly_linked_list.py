from doubly_linked_list import DoubleLinkedList


def test_constructor():
    items = ("duck", 3, [2, 3, 4], object())
    dll = DoubleLinkedList(items)
    dll2 = DoubleLinkedList()
    for i in items[::-1]:
        dll2.insert(i)
    for i in items:
        assert dll.pop() == dll2.pop()


def test_insert():
    dll = DoubleLinkedList()
    dll.insert(5)
    assert dll.pop() == 5


def test_pop():
    dll = DoubleLinkedList(("dog", 3, "fish taco", object(), "house"))
    assert "dog" == dll.pop()


def test_shift():
    dll = DoubleLinkedList(("dog", 3, "fish taco", object(), "house"))
    assert "house" == dll.shift()


def test_size():
    dll = DoubleLinkedList(("dog", 3, "fish taco", object(), "house"))
    assert dll.size() == 5


def test_remove():
    dll = DoubleLinkedList(("dog", 3, "fish taco", object(), "house"))
    dll.remove("fish taco")
    assert dll.size() == 4

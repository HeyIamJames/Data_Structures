from heap import BinaryHeap


def test_push():
    heap = BinaryHeap((1, 3, 8, 26, 4, 15, 20, 88, 23, 7, 11, 40))
    assert heap.heapList[1] == 1
    assert heap.heapList[4] == 23
    # assert heap.heapList[3] == 6


def test_pop():
    heap = BinaryHeap((1, 3, 8, 26, 4, 15, 20, 88, 23, 7, 11, 40))
    heap.pop()
    assert heap.heapList[1] == 3
    assert heap.heapList[-2] == 40
    heap.pop()

class Node(object):
    """Creates a node"""
    def __init__(self, value=None, nextNode=None, prevNode=None):
        self.value = value
        self.nextNode = nextNode
        self.prevNode = prevNode


class DoubleLinkedList(object):

    def __init__(self, iterable=None):
        """
        Constructor:
          Accepts optional iterable
          LinkedList((1, 2, 3)) --> (1, 2, 3)
        """
        self._size = 0
        self.first = None
        self.last = None
        if iterable:
            self.first = Node(iterable[0], None)
            node = self.first
            self._size += 1
            for val in iterable[1:]:
                node.nextNode = Node(val, None)
                node.nextNode.prevNode = node
                node = node.nextNode
                self.last = node
                self._size += 1

    def insert(self, val):
        """
        insert method:
          adds new value to the head of the list
        """
        if self.first is None:
            self.first = Node(val)
            self.last = self.first
        self.first.prevNode = Node(val, self.first, None)
        self.first = self.first.prevNode
        self._size += 1

    def pop(self):
        """
        pop method:
           removes the value at the head of the list and returns it
        """
        node = self.first
        self.first = self.first.nextNode
        if self.first is not None:
            self.first.prevNode = None
        self._size -= 1
        return node.value

    def shift(self):
        """
        pop method:
           removes the value at the tail of the list and returns it
        """
        node = self.last
        self.last = self.last.prevNode
        if self.last is not None:
            self.last.nextNode = None
        self._size -= 1
        return node.value

    def size(self):
        return self._size

    def remove(self, val):
        """
        remove method:
          removes given node from list
        """
        node = self.first
        while node.value != val:
            node = node.nextNode
            if node is None:
                raise ValueError(repr(val) + "Val not in DoublyLinkedList")
        node.nextNode.prefNode = node.prevNode
        node.prevNode.nextNode = node.nextNode
        self._size -= 1

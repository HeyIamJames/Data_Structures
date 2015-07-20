from linked_list import Node

class Queue(object):
    def __init__(self):
        self._size = 0
        self.first = None
        self.last = None

    def enqueue(self, val):
        """
        enqueue method:
          adds new value to the end of the list
        """
        if self._size == 0:
            self.first = Node(val, None)
            self.last = self.first
        else:
            self.last.nextNode = Node(val, None)
            self.last = self.last.nextNode
        self._size += 1

    def dequeue(self):
        """
        dequeue method:
           removes the value at the head of the list and returns it
        """
        node = self.first
        self.first = self.first.nextNode
        self._size -= 1
        return node.value

    def size(self):
        return self._size

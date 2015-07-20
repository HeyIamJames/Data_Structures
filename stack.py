from linked_list import LinkedList

class Stack(object):
    def __init__(self, iterable=None):
        self._list = LinkedList(iterable)

    def push(self, val):
        self._list.insert(val)

    def pop(self):
        return self._list.pop()


# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class Node(object):
    def __init__(self, val, pointer, priority=0):
        self.value = val
        self.nextNode = pointer
        self.priority = priority


class PriorityQueue(object):
    def __init__(self):
        self._size = 0
        self.first = None

    def restructure(self, node):
        """
        restructure method:
          moves the node down the list untill it outranks
          it's nextNode.
        """
        prev_node = None
        while True:
            if node.nextNode.priority >= node.priority:
                prev_node = node.nextNode
                node.nextNode = node.nextNode.nextNode
                if node.nextNode is None:
                    prev_node.nextNode = node
                    break
            elif prev_node is None:
                self.first = node
                break
            else:
                prev_node.nextNode = node
                break

    def insert(self, val, priority=0):
        """
        insert method:
          adds new value to the front of the list
          and then calls the restructure method
          which makes sure the node is in the right spot
        """
        if self.first is None:
            self.first = Node(val, None, priority)
        else:
            self.restructure(Node(val, self.first, priority))
        self._size += 1

    def pop(self):
        """
        pop method:
           removes the value at the head of the list and returns it
        """
        node = self.first
        if self.first.nextNode is not None:
            self.first = self.first.nextNode
        else:
            self.first = None
        self._size -= 1
        return node.value

    def size(self):
        return self._size

    def peek(self):
        return self.first.value

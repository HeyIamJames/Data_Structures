class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value=value
        self.nextNode=pointer

class LinkedList(object):
    def __init__(self, iterable=None): 
        """
        Constructor:
          Accepts optional iterable
          LinkedList((1, 2, 3)) --> (1, 2, 3)
        """
        self._size = 0
        self.first = None
        if iterable:
            self.first = Node(iterable[0], None)
            node=self.first
            self._size += 1
            for val in iterable[1:]:
                node.nextNode = Node(val, None)
                node = node.nextNode
                self._size += 1

    def insert(self, val): 
        """
        insert method:
          adds new value to the head of the list
        """
        self.first = Node(val, self.first)
        self._size += 1

    def pop(self): 
        """
        pop method:
           removes the value at the head of the list and returns it
        """
        node=self.first
        self.first = self.first.nextNode
        self._size -= 1
        return node.value
        
    def size(self): 
        return self._size

    def search(self, val):
        """
        search method:
          returns the first node in the list with the given value
        """
        node = self.first
        while not node is None:
            if val == node.value:
                break
            else: node = node.nextNode
        return node

    def remove(self, node): #remove node without index
        """
        remove method:
          removes given node from list
        """
        if self.first is node:
            self.first = self.first.nextNode
            self._size -= 1
        else:
            myNode = self.first
            while not myNode is None:
                if myNode.nextNode is node:
                    myNode.nextNode = myNode.nextNode.nextNode
                    self._size -= 1
                else:
                    myNode = myNode.nextNode
            

    def display(self):
        """
        display method
          returns string of list as though it were a tuple
        """
        if self._size == 0: return "()"
        else:
            s  = "("+repr(self.first.value)
            node = self.first.nextNode
            while not node is None:
                s += ", "+repr(node.value)
                node=node.nextNode
            return s+")"

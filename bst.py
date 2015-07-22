from __future__ import unicode_literals
#source of info http://interactivepython.org/runestone/static/pythonds/Trees/bst.html

class Node(object):
    def __init__(self, val, left=None, right=None, parent=None):
        """Instantiates a node"""
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    # def depth_helper(self):
    #     left_depth = self.left.depth() if self.left else 0
    #     right_depth = self.right.depth() if self.right else 0
    #     return ((left_depth + 1), (right_depth + 1))

    def depth(self):
        left_depth = self.left.depth() if self.left else 0
        right_depth = self.right.depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    def get_dot(self):
            """return the tree with root 'self' as a dot graph for visualization"""
            return "digraph G{\n%s}" % ("" if self.val is None else (
                "\t%s;\n%s\n" % (
                    self.val,
                    "\n".join(self._get_dot())
                )
            ))

    def _get_dot(self):
        """recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.val, self.left.val)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.val, self.right.val)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.val, r)


class BinarySearchTree(object):
    root = None
    def __init__(self):
        """Initialize a binary search tree"""
        self.root = None
        self.set = set()

    def insert(self, val):
        """Insert a node, checks if duplicate"""
        if val not in self.set:
            if not self.root:
                self.root = Node(val)
            else:
                current = self.root
                while current:
                    if val < current.val:
                        if current.left is None:
                            current.left = Node(val, parent=current)
                            break
                        current = current.left
                    else:
                        if current.right is None:
                            current.right = Node(val, parent=current)
                            break
                        current = current.right
            self.set.add(val)

    def contains(self, val):
        """Return a True/False if node in the tree"""
        return val in self.set

    def size(self):
        """Return number of items in  tree"""
        return len(self.set)

    def depth(self):
        """Return number of levels in tree"""
        if self.root:
            return self.root.depth()

    def balance(self):
        """If more values on right returns 1, if left -1. Else 0"""
        if self.depth == 1:
            return 0
        elif self.root.right_depth > self.depth.left_depth:
            return 1
        else:
            return -1


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(9)
    tree.insert(2)
    tree.insert(1)


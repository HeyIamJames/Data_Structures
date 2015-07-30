"""
sources:

http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
http://www.quora.com/How-do-I-create-my-own-Hash-Table-implementation-in-Python
"""
class Hash_table:
    def __init__(self, size):
        self.size = size
        self.table = [[] for x in xrange(size)]


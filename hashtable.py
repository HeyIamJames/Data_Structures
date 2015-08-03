from termcolor import colored
"""
sources:

http://interactivepython.org/runestone/static/pythonds/SortSearch/Hashing.html
http://www.quora.com/How-do-I-create-my-own-Hash-Table-implementation-in-Python
"""


class HashTable:
    def __init__(self, size):
        '''hashtable utilizing chaining'''
        self.size = size
        self.hashtable = [[] for x in xrange(size)]

    def hash(self, key):
        """returns hashed value of key"""
        hashing_value = 0
        for i in key:
            hashing_value += ord(i)
        hashing_algorithm = hashing_value % self.size
        return hashing_algorithm

    def get(self, key):
        """return value of key"""
        hash_key = self.hash(key)
        bucket = self.hashtable[hash_key]
        for item in reversed(bucket):
            if item[0] == key:
                return item[1]

    def set(self, key, value):
        """adds key/val into hash table"""
        if type(key) == str:
            hashed_key = self.hash(key)
            self.hashtable[hashed_key].append((key, value))
        else:
            raise TypeError('non-string provided')

    # debugging tool
    def contents(self):
        """returns key/values of hash table"""
        for i in self.hashtable:
            if i:
                print colored("[", "red")
                for x in i:
                    print "(", colored(x[0], 'green'), ",", colored(x[1], 'blue'),")"
                print colored("]", "red")
            else:
                print colored(i, "red")


if __name__ == '__main__':
    x = HashTable(16)
    x.set('k', 20)
    x.set('s', 7)
    x.set('j', 99)
    x.set('o', 12)
    print x.get('k')
    print x.get('j')
    print x.hash('k')
    print x.contents()

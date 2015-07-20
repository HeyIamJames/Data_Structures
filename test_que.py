# enqueue(value): adds value to the queue
# dequeue(): removes the correct item from the queue and returns its value
# (should raise an error if the queue is empty)
# size(): return the size of the queue.  Should return 0 if the queue is empty.

import pytest
from queue import Queue

que = [1, 2, 3, 4, 5]


def test_enque():
    q = Queue()
    for n in que:
        q.enqueue(n)
    q.enqueue(6)
    assert q.size() == 6

def test_dequeue():
    q = Queue()
    for n in que:
        q.enqueue(n)
    assert q.dequeue() == 1
    assert q.size() == 4

def test_size():
    q = Queue()
    for n in que:
        q.enqueue(n)
        assert q.size() == n

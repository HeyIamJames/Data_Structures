# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from priority_que import PriorityQueue


def makeapq():
    pq = PriorityQueue()
    pq.insert("duck", 2)
    pq.insert(3, 1)
    pq.insert("fish", 5)
    pq.insert("money", 5)
    pq.insert(4, 2)
    return pq


def test_insert():
    pq = makeapq()
    assert pq.first.value == "fish"


def test_pop():
    pq = makeapq()
    assert ["fish", "money", "duck", 4, 3] == [pq.pop() for x in range(5)]


def test_peek():
    pq = makeapq()
    assert pq.peek() == "fish"
    pq.pop()
    assert pq.peek() == "money"

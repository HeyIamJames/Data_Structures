from radix_sort import radixsort
from random import shuffle
import pytest


def test_randoms():
    x = range(100)
    randoms = x[:]
    shuffle(randoms)
    radixsort(randoms)
    y = randoms
    assert x == y


def test_empty():
    x = []
    y = x
    radixsort(x)
    assert x == y


def test_reversed():
    x = []
    for i in range(1, 10):
        x.append(i)
    y = []
    for i in reversed(x):
        y.append(i)
    radixsort(y)
    z = y
    assert z == x


def test_ordered():
    x = []
    for i in range(1, 10):
        x.append(i)
    radixsort(x)
    z = x
    assert z == x


def test_string():
    with pytest.raises(ValueError):
        radixsort('cat')


def test_badinput():
    with pytest.raises(TypeError):
        radixsort('bad', 123, [6, 7], ('hi', 2))
        

#test non valid inputs,different lengths of integers, already sorted
# py.test -q test_radix.py

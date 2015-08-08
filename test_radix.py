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


def tset_reversed():
    x = []
    for i in range(1, 10):
        x.append(i)
    y = reversed(x)
    z = radixsort(y)
    assert z == x


def test_ordered():
    pass


def test_string():
    with pytest.raises(ValueError):
        radixsort('cat')


#test non valid inputs,different lengths of integers, already sorted

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


def test_various_length():
    x = [1, 200, 600, 1234567, 99999, 7]
    radixsort(x)
    y = x
    expected = [1, 7, 200, 600, 99999, 1234567]
    assert expected == y


def test_string():
    with pytest.raises(ValueError):
        radixsort('cat')


def test_badinput():
    with pytest.raises(TypeError):
        radixsort('bad', 123, [6, 7], ('hi', 2))

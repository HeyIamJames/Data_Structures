from sorting_quicksort import quicksort
from random import shuffle
import pytest


def test_randoms():
    x = range(100)
    randoms = x[:]
    shuffle(randoms)
    quicksort(randoms)
    y = randoms
    assert x == y


def test_string():
    with pytest.raises(TypeError):
        quicksort('cat')


def test_empty():
    x = []
    y = x
    quicksort(x)
    assert x == y


def test_reversed():
    x = []
    for i in range(1, 10):
        x.append(i)
    y = []
    for i in reversed(x):
        y.append(i)
    quicksort(y)
    z = y
    assert z == x


def test_ordered():
    x = []
    for i in range(1, 10):
        x.append(i)
    quicksort(x)
    z = x
    assert z == x


def test_various_length():
    x = [1, 200, 600, 1234567, 99999, 7]
    quicksort(x)
    y = x
    expected = [1, 7, 200, 600, 99999, 1234567]
    assert expected == y


def test_badinput():
    with pytest.raises(TypeError):
        quicksort('bad', 123, [6, 7], ('hi', 2))


def test_best():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quicksort(x)
    expected = sorted(x)
    assert expected == x

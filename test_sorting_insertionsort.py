from sorting import insertion_sort
from random import shuffle
import pytest


def test_randoms():
    x = range(100)
    randoms = x[:]
    shuffle(randoms)
    insertion_sort(randoms)
    y = randoms
    assert x == y


def test_string():
    with pytest.raises(TypeError):
        insertion_sort('cat')


def test_empty():
    x = []
    y = x
    insertion_sort(x)
    assert x == y


def test_reversed():
    x = []
    for i in range(1, 10):
        x.append(i)
    y = []
    for i in reversed(x):
        y.append(i)
    insertion_sort(y)
    z = y
    assert z == x


def test_ordered():
    x = []
    for i in range(1, 10):
        x.append(i)
    insertion_sort(x)
    z = x
    assert z == x


def test_various_length():
    x = [1, 200, 600, 1234567, 99999, 7]
    insertion_sort(x)
    y = x
    expected = [1, 7, 200, 600, 99999, 1234567]
    assert expected == y


def test_badinput():
    with pytest.raises(TypeError):
        insertion_sort('bad', 123, [6, 7], ('hi', 2))


def test_best():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    insertion_sort(x)
    expected = sorted(x)
    assert expected == x

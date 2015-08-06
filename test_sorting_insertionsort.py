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

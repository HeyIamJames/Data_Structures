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


def test_string():
    with pytest.raises(ValueError):
        radixsort('cat')

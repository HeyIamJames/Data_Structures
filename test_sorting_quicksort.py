from sorting_quicksort import quicksort
from random import shuffle


def test_randoms():
    x = range(100)
    randoms = x[:]
    shuffle(randoms)
    quicksort(randoms)
    y = randoms
    assert x == y

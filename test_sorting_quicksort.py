from sorting_quicksort import quicksort
from random import shuffle


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

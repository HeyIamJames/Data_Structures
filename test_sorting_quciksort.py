from sorting_quicksort import quicksort
import pytest


@pytest.fixture
def test_list():
    y = [5, 6, 4, 10, 17, 13, 99, 1, 50]
    return y


def test_sort(test_list):
    assert quicksort(test_list) == [1, 4, 5, 6, 10, 13, 17, 50, 99]

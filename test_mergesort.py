import random
from merge_sort import mergesort


def test_worst_case():
    worst_case = [i for i in range(1, 100) if i % 2] + \
        [i for i in range(1, 100) if not i % 2]
    assert mergesort(worst_case) == range(1, 100)


def test_normal_case():
    normal_case = [random.randint(0, 100) for i in range(15)]
    assert mergesort(normal_case) == sorted(normal_case)


def test_repeating_list():
    repeating = [4] * 30
    assert mergesort(repeating) == [4] * 30


def test_sorted_list():
    presorted = range(30)
    assert mergesort(presorted) == presorted


def test_reversed_sorted():
    backwards_sort = range(30, -1, -1)
    assert mergesort(backwards_sort) == range(31)


def test_empty_list():
    assert mergesort([]) == []


def test_list_len_one():
    assert mergesort([2]) == [2]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random


def quicksort(_list):
    if len(_list) > 1:
        helper(_list, 0, len(_list) - 1)
    else:
        return _list


def helper(_list, first, last):
    if first < last:
        splitpoint = partition(_list, first, last)
        helper(_list, first, splitpoint - 1)
        helper(_list, splitpoint + 1, last)


def partition(_list, first, last):
    pivot = _list[first]
    leftcounter = first + 1
    rightcounter = last
    done = False
    while not done:

        while leftcounter <= rightcounter and _list[leftcounter] <= pivot:
            leftcounter = leftcounter + 1

        while _list[rightcounter] >= pivot and rightcounter >= leftcounter:
            rightcounter = rightcounter - 1

        if rightcounter < leftcounter:
            done = True
        else:
            temp = _list[leftcounter]
            _list[leftcounter] = _list[rightcounter]
            _list[rightcounter] = temp

    temp = _list[first]
    _list[first] = _list[rightcounter]
    _list[rightcounter] = temp

    return rightcounter


def test_bad():
    x = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
    quicksort(x)


def test_best():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    quicksort(x)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit('test_bad()', setup='from __main__ import test_bad', number=1))
    print(timeit.timeit('test_best()', setup='from __main__ import test_best', number=1))

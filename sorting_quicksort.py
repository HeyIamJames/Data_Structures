# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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

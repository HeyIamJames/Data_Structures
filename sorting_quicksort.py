# -*- coding: utf-8 -*-
from __future__ import unicode_literals


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

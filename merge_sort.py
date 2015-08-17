from timeit import timeit
from random import shuffle


def mergesort(l):
    if len(l) <= 1:
        return l
    else:
        middle = len(l) // 2
        left = l[:middle]
        right = l[middle:]
        return merge(mergesort(left), mergesort(right))


def merge(left, right):
    merged = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged.append(right[j])
            j += 1
        else:
            merged.append(left[i])
            i += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

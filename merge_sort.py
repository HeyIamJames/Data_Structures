import random


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


def test_bad():
    x = []
    for i in range(10):
        x.append(random.randrange(100))
    mergesort(x)


def test_best():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    mergesort(x)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit('test_bad()', setup='from __main__ import test_bad', number=1))
    print(timeit.timeit('test_best()', setup='from __main__ import test_best', number=1))

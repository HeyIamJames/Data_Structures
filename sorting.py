import random


def insertion_sort(l):
    for i in range(1, len(l)):
        key_value = l[i]
        scan_pos = i - 1
        while (scan_pos >= 0) and (l[scan_pos] > key_value):
            l[scan_pos + 1] = l[scan_pos]
            scan_pos = scan_pos - 1
        l[scan_pos + 1] = key_value


def test_bad():
    x = []
    for i in range(10):
        x.append(random.randrange(100))
    insertion_sort(x)


def test_best():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    insertion_sort(x)


if __name__ == '__main__':
    import timeit
    print(timeit.timeit('test_bad()', setup='from __main__ import test_bad', number=1))
    print(timeit.timeit('test_best()', setup='from __main__ import test_best', number=1))

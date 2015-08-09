from __future__ import print_function
import random


def insertion_sort(list):
    for i in range(1, len(list)):
        key_value = list[i]
        scan_pos = i - 1
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1
        list[scan_pos + 1] = key_value


def print_list(list):
    for item in list:
        print("{:3}".format(item), end="")
    print()

list = []
for i in range(10):
    list.append(random.randrange(100))

print_list(list)
insertion_sort(list)
print_list(list)


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

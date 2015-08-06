import random


def radixsort(_list):
    slots = 10
    max_length = False
    holder, placement = -1, 1

    for i, n in enumerate(_list):
        if n < 0:
            raise ValueError('only accepts postive integers')
        _list[i] = int(n)

    while not max_length:
        max_length = True
        buckets = [list() for _ in range(slots)]

        for i in _list:
            holder = i // placement
            buckets[holder % slots].append(i)
            if max_length and holder > 0:
                max_length = False

        a = 0
        for b in range(slots):
            buck = buckets[b]
            for i in buck:
                _list[a] = i
                a += 1
        placement *= slots

x = []
for i in range(10):
    x.append(random.randrange(100))

y = [3, 123.2, 32, 5]

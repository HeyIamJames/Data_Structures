from __future__ import print_function
import random

def selection_sort(list):
    for i in range(len(list)):
        x = i
        for scan_pos in range(i + 1, len(list)):
            if list[scan_pos] < list[x]:
                x = scan_pos
        temp = list[x]
        list[x] = list[i]
        list[i] = temp
 
def print_list(list):
    for item in list:
        print("{:3}".format(item), end="")
    print()

list = []
for i in range(10):
    list.append(random.randrange(100))

print_list(list)
selection_sort(list)
print_list(list)

def insertion_sort(list):
    for i in range(1, len(list)):
        key_value = list[i]
        scan_pos = i - 1
        while (scan_pos >= 0) and (list[scan_pos] > key_value):
            list[scan_pos + 1] = list[scan_pos]
            scan_pos = scan_pos - 1
        list[scan_pos + 1] = key_value

list = []
for i in range(10):
    list.append(random.randrange(100))

print_list(list)
insertion_sort(list)
print_list(list)


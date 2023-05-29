
from random import randint


def selection_sort(array):
    for i in range(len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array


arr = [randint(1, 100) for _ in range(10)]

print(f"\nUnsorted array:\n{arr}\n")

print(f"Sorted array:\n{selection_sort(arr)}\n")

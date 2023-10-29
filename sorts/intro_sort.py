"""
Introspective Sort is hybrid sort (Quick Sort + Heap Sort + Insertion Sort)
if the size of the list is under 16, use insertion sort
https://en.wikipedia.org/wiki/Introsort
"""
import math


def insertion_sort(array: list, start: int = 0, end: int = 0) -> list:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> insertion_sort(array, 0, len(array))
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    """
    end = end or len(array)
    for i in range(start, end):
        temp_index = i
        temp_index_value = array[i]
        while temp_index != start and temp_index_value < array[temp_index - 1]:
            array[temp_index] = array[temp_index - 1]
            temp_index -= 1
        array[temp_index] = temp_index_value
    return array


def heapify(array: list, index: int, heap_size: int) -> None:  # Max Heap
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> heapify(array, len(array) // 2 ,len(array))
    """
    largest = index
    left_index = 2 * index + 1  # Left Node
    right_index = 2 * index + 2  # Right Node

    if left_index < heap_size and array[largest] < array[left_index]:
        largest = left_index

    if right_index < heap_size and array[largest] < array[right_index]:
        largest = right_index

    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        heapify(array, largest, heap_size)


def heap_sort(array: list) -> list:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> heap_sort(array)
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    """
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, i, n)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, 0, i)

    return array


def median_of_3(
    array: list, first_index: int, middle_index: int, last_index: int
) -> int:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> median_of_3(array, 0, 0 + ((len(array) - 0) // 2) + 1, len(array) - 1)
    12

    >>> array = [13, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> median_of_3(array, 0, 0 + ((len(array) - 0) // 2) + 1, len(array) - 1)
    13

    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 15, 14, 27, 79, 23, 45, 14, 16]

    >>> median_of_3(array, 0, 0 + ((len(array) - 0) // 2) + 1, len(array) - 1)
    14
    """
    if (array[first_index] > array[middle_index]) != (
        array[first_index] > array[last_index]
    ):
        return array[first_index]
    elif (array[middle_index] > array[first_index]) != (
        array[middle_index] > array[last_index]
    ):
        return array[middle_index]
    else:
        return array[last_index]


def partition(array: list, low: int, high: int, pivot: int) -> int:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> partition(array, 0, len(array), 12)
    8
    """
    i = low
    j = high
    while True:
        while array[i] < pivot:
            i += 1
        j -= 1
        while pivot < array[j]:
            j -= 1
        if i >= j:
            return i
        array[i], array[j] = array[j], array[i]
        i += 1


def sort(array: list) -> list:
    """
    :param collection: some mutable ordered collection with heterogeneous
    comparable items inside
    :return: the same collection ordered by ascending

    Examples:
    >>> sort([4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12])
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]

    >>> sort([-1, -5, -3, -13, -44])
    [-44, -13, -5, -3, -1]

    >>> sort([])
    []

    >>> sort([5])
    [5]

    >>> sort([-3, 0, -7, 6, 23, -34])
    [-34, -7, -3, 0, 6, 23]

    >>> sort([1.7, 1.0, 3.3, 2.1, 0.3 ])
    [0.3, 1.0, 1.7, 2.1, 3.3]

    >>> sort(['d', 'a', 'b', 'e', 'c'])
    ['a', 'b', 'c', 'd', 'e']
    """
    if len(array) == 0:
        return array
    max_depth = 2 * math.ceil(math.log2(len(array)))
    size_threshold = 16
    return intro_sort(array, 0, len(array), size_threshold, max_depth)


def intro_sort(
    array: list, start: int, end: int, size_threshold: int, max_depth: int
) -> list:
    """
    >>> array = [4, 2, 6, 8, 1, 7, 8, 22, 14, 56, 27, 79, 23, 45, 14, 12]

    >>> max_depth = 2 * math.ceil(math.log2(len(array)))

    >>> intro_sort(array, 0, len(array), 16, max_depth)
    [1, 2, 4, 6, 7, 8, 8, 12, 14, 14, 22, 23, 27, 45, 56, 79]
    """
    while end - start > size_threshold:
        if max_depth == 0:
            return heap_sort(array)
        max_depth -= 1
        pivot = median_of_3(array, start, start + ((end - start) // 2) + 1, end - 1)
        p = partition(array, start, end, pivot)
        intro_sort(array, p, end, size_threshold, max_depth)
        end = p
    return insertion_sort(array, start, end)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    user_input = input("Enter numbers separated by a comma : ").strip()
    unsorted = [float(item) for item in user_input.split(",")]
    print(sort(unsorted))

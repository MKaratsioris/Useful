from random import random, randint
from median_finding import median_of_medians

"""
    Divide-and-Conquer Algorithm

    The input is an iterable of sorted elements. If an element
    you are looking for is in that sorted iterable, the algorithm 
    will return its position. Otherwise, the algorithm will return None.

    Time Complexity:    O(N * logN)
    Space Complexity:   O(logN) / O(N)
    
    TODO    Return additionally the number of iterations/steps the algorithm performs.
"""

iterations: int = 0

def quick_sort(iterable: list) -> list:
    """
    Quick Sort Algorithm
    
    Quicksort has a smaller constant than merge sort. So if they’re both O(N * logN) time, quicksort is faster. 
    And quicksort is faster in practice because it hits the average case way more often than the worst case, 
    which is O(N * N). The performance of quicksort heavily depends on the pivot you choose.
    
    Time Complexity: O(N * logN) [worst case is O(N * N)]
    Space Complexity: O(1)

    Parameters
    ----------
    iterable : list
        Unsorted collection of elements

    Returns
    -------
    tuple[list, int]
        A tuple with the sorted collection of elements and the number of steps it took to conclude the sorting.
    """
    global iterations
    if len(iterable) < 2:
        iterations += 1
        return iterable
    if len(iterable) == 2:
        iterations += 1
        if iterable[0] > iterable[1]:
            iterable[0], iterable[1] = iterable[1], iterable[0]
            return iterable
        return iterable
    pivot = iterable[(len(iterable)) // 2]
    #pivot = median_of_medians(iterable, len(iterable) // 2)
    left_sublist: list = [element for element in iterable[1:] if element <= pivot]
    right_sublist: list = [element for element in iterable[1:] if element > pivot]
    iterations += 1
    return quick_sort(iterable=left_sublist) + [pivot] + quick_sort(iterable=right_sublist)


def generate_random_numbers(size: int, max_value: int) -> list[int]:
    numbers: list = [int(random() * randint(0, max_value)) for _ in range(size)]
    return numbers

if __name__ == '__main__':
    size: int = 10
    max_value: int = 1_000
    numbers: list = generate_random_numbers(size=size, max_value=max_value)
    print(f"Before sorting: {numbers=}")
    sorted_numbers = quick_sort(iterable=numbers)
    print(f"After sorting: {numbers=}")
    print(f"{sorted_numbers=}")
    print(f"{iterations=}")
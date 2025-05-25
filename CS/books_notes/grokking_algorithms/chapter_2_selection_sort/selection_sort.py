from random import random, randint

"""
Problem: Suppose you have a bunch of music on your computer and for each artist, you have a play count. You want to sort this list from most to least played, so that you can rank your favorite artists.

Solution: One way is to go through the list and find the most-played artist. Add that artist to a new list. Do it again to ind the next-most-played artist. Keep doing this, and you'll end up with a sorted list.

Time Complexity: O(N*N)
Space Complexity: O(1)

Number of steps: N * (N - 1) / 2
"""

def selection_sort(iterable: list) -> tuple[list, int]:
    """
    Selection Sort Algorithm
    
    Time Complexity: O(N*N)
    Space Complexity: O(1)

    Parameters
    ----------
    iterable : list
        Unsorted collection of elements

    Returns
    -------
    tuple[list, int]
        A tuple with the sorted collection of elements and the number of iterations it took to conclude the sorting.
    """
    sorted_list = []
    number_iterations: int = 0
    for _ in range(len(iterable)):        
        smallest_element = iterable[0]
        smallest_index: int = 0
        for i in range(1, len(iterable)):
            number_iterations += 1
            if iterable[i] < smallest_element:
                smallest_element = iterable[i]
                smallest_index = i        
        sorted_list.append(iterable.pop(smallest_index))
    return sorted_list, number_iterations

def generate_random_numbers(size: int, max_value: int) -> list[int]:
    numbers: list = [int(random() * randint(0, max_value)) for _ in range(size)]
    return numbers


if __name__ == '__main__':
    size: int = 10
    max_value: int = 1_000
    numbers: list = generate_random_numbers(size=size, max_value=max_value)
    print(f"Before sorting: {numbers=}")
    sorted_numbers, steps = selection_sort(iterable=numbers)
    print(f"After sorting: {numbers=}")
    print(f"{sorted_numbers=}")
    print(f"{steps=}")
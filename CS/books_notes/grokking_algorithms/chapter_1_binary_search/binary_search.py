from typing import Union

def binary_search(sorted_list: list, item: Union[int, str, bool]) -> Union[tuple[int, int], None]:
    """
    Binary Search Algorithm
    -----------------------

    The input is an iterable of sorted elements. If the element you are looking for is in that sorted iterable, the algorithm  will return its position. Otherwise, the algorithm will return None.

    Time Complexity:    O(logN)
    Space Complexity:   O(1)
    
    Attributes
    ----------
    sorted_list : list
        Sorted collection of elements to search for the item
    item : int | str | bool
        Item to search in the sorted_list
    
    Returns
    -------
    tuple[int, int] | None
        A tuple with the position of the item in the sorted_list as well as the number of steps it took to conclude the search or None
    """
    low: int = 0
    high: int = len(sorted_list) - 1
    steps: int = 1
    while low <= high:
        middle: int = (high + low) // 2
        guess = sorted_list[middle]
        if guess == item:
            return middle, steps
        elif guess < item:
            low = middle + 1
        elif guess > item:
            high = middle - 1
        steps += 1
    return None

if __name__ == "__main__":
    #for maximum in range(1025):
        #print(f"Number of elements: {maximum}")
    maximum = 1_025
    guess = maximum - 1
    numbers: list[int] = [number for number in range(maximum)]
    index, steps = binary_search(numbers, guess)
    print(f"\n{maximum=}\t{index=}\t{steps=}\n")
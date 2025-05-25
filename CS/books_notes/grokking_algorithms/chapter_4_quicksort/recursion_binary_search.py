from typing import Union

def binary_search_recursion(sorted_iterable: Union[list, tuple, set], item: Union[int, str]) -> Union[int, None]:
    """
    Binary Search Recursive Algorithm
    ---------------------------------

    The input is an iterable of sorted elements. If the element you are looking for is in that sorted iterable, the algorithm will return its position. Otherwise, the algorithm will return None.

    Time Complexity:    O(logN)
    Space Complexity:   O(1)
    
    Attributes
    ----------
    sorted_iterable : list | tuple | set
        Sorted elements to search for the item
    item : int | str | bool
        Item to search in the sorted_iterable
    
    Returns
    -------
    int | None
        Position of the item in the sorted_iterable
    """
    if len(sorted_iterable) == 1:
        if sorted_iterable[0] == item:
            return sorted_iterable[0]
        return None
    low: int = 0
    high: int = len(sorted_iterable) - 1
    middle: int = (high + low) // 2
    guess = sorted_iterable[middle]
    if guess == item:
        return middle
    elif guess < item:
        return binary_search_recursion(sorted_iterable=sorted_iterable[middle + 1:], item=item)
    elif guess > item:
        return binary_search_recursion(sorted_iterable=sorted_iterable[:middle - 1], item=item)

if __name__ == "__main__":
    #for maximum in range(1025):
        #print(f"Number of elements: {maximum}")
    maximum = 1_025
    guess = maximum - 1
    numbers: list[int] = [number for number in range(maximum)]
    index = binary_search_recursion(numbers, guess)
    print(f"\n{maximum=}\t{index=}\n")
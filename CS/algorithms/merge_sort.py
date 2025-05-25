def merge_sort(arr: list) -> list:
    """

    :param arr:
    :return:
    """
    # If the input array has fewer than 2 elements, it is already sorted
    if len(arr) < 2:
        return arr

    # Split the array in half
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort the two halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves and return the result
    return merge(left, right)


def merge(left: list, right: list) -> list:
    # Initialize an empty result list
    result = []

    # While there are elements in both lists
    while left and right:
        # In case the first element of the left list is smaller, append it to the result and remove it from the left list
        if left[0] < right[0]:
            result.append(left.pop(0))
        # Otherwise, append the first element of the right list to the result and remove it from the right list
        else:
            result.append(right.pop(0))

        # Append any remaining elements from the left list to the result
        result.extend(left)

        # Append any remaining elements from the right list to the result
        result.extend(right)

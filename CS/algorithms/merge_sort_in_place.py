def merge_sort_in_place(arr, start, end):
    # If the input array has fewer than 2 elements, it is already sorted
    if end - start < 1:
        return

    # Split the array in half
    mid = (start + end) // 2

    # Recursively sort the two halves
    merge_sort_in_place(arr, start, mid)
    merge_sort_in_place(arr, mid + 1, end)

    # Merge the sorted halves
    return merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    # Initialize indices for the left and right halves
    left_index = start
    right_index = mid + 1

    # While there are elements in both halves
    while left_index <= mid and right_index <= end:
        # If the element at the left index is smaller, increment the left index
        if arr[left_index] <= arr[right_index]:
            left_index += 1
        # Otherwise, move the element at the right index to the left side of the array and increment the right index
        else:
            value = arr.pop(right_index)
            arr.insert(left_index, value)
            left_index += 1
            mid += 1



# Example usage
arr_1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
merge_sort_in_place(arr_1, 0, len(arr_1) - 1)

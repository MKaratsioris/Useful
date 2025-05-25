def ternary_search(array, target):
    left = 0
    right = len(array) - 1

    def ternary_search_implementation(array, target, left, right):
        # Check if the array is empty
        if left > right:
            return -1
        partition_size = round((right - left) / 3)
        mid1 = left + partition_size
        mid2 = right - partition_size

        if array[mid1] == target:
            return mid1
        if array[mid2] == target:
            return mid2

        # Check if the target is in the middle part
        if array[mid1] < target and array[mid2] > target:
            return ternary_search_implementation(array, target, mid1 + 1, mid2 - 1)

        # Check if the target is in the right part
        if array[mid2] < target:
            return ternary_search_implementation(array, target, mid2 + 1, right)

        # Check if the target is in the left part
        if array[mid1] > target:
            return ternary_search_implementation(array, target, left, mid1 - 1)

    return ternary_search_implementation(array, target, left, right)
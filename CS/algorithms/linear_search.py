import time


def timeit(func):
    """
    Decorator for measuring function's running time.
    This function can be used when running script outside PyCharm.
    """

    def measure_time(*args, **kw):
        start_time = time.time()
        result = func(*args, **kw)
        print("Processing time of %s(): %.5f seconds."
              % (func.__qualname__, time.time() - start_time))
        return result

    return measure_time


@timeit
def linear_search(list_name, target):
    """
    By using the linear search method, it returns the index position
    of the target if found, else returns None.
    """

    for i in range(len(list_name)):
        if list_name[i] == target:
            return i
    return None


def verify(index):
    """
    Prints out if the target is inside the list or not.
    """

    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target was not found in the given list.")


# # 10^(1) => 0.00000 sec
# test_list = [x for x in range(11)]
# test_target = 10
# verify(linear_search(test_list, test_target))

# # 10^(2) => 0.00000 sec
# test_list = [x for x in range(101)]
# test_target = 100
# verify(linear_search(test_list, test_target))

# # 10^(3) => 0.00000 sec
# test_list = [x for x in range(1001)]
# test_target = 1000
# verify(linear_search(test_list, test_target))

# # 10^(4) => 0.00000 sec
# test_list = [x for x in range(10001)]
# test_target = 10000
# verify(linear_search(test_list, test_target))

# # 10^(5) => 0.00300 sec (varies...)
# test_list = [x for x in range(100001)]
# test_target = 100000
# verify(linear_search(test_list, test_target))

# # 10^(6) => 0.03000 sec (varies...)
# test_list = [x for x in range(1000001)]
# test_target = 1000000
# verify(linear_search(test_list, test_target))

# # 10^(7) => 0.30000 sec (varies...)
# test_list = [x for x in range(10000001)]
# test_target = 10000000
# verify(linear_search(test_list, test_target))

# # 10^(8) => 3.00000 sec (varies...)
# test_list = [x for x in range(100000001)]
# test_target = 100000000
# verify(linear_search(test_list, test_target))

# # 10^(9) => 300.00000 sec (varies...) ?????????????????
# test_list = [x for x in range(1000000001)]
# test_target = 1000000000
# verify(linear_search(test_list, test_target))

# import sys
# print("Maximum size of an integer: ",sys.maxsize) => 2147483647

# 10^(10) =>
# test_list = [x for x in range(10000000001)]
# test_target = 10000000000
# verify(linear_search(test_list, test_target))

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        result = func(*args, **kwargs)
        delta = time.perf_counter_ns() - start
        print(f"Function: {func.__name__}  [{delta:,.3f} ns]")
        return result
    return wrapper

@timer
def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    n = 10
    factorial = factorial(n)
    print(f"{n}! = {factorial}")
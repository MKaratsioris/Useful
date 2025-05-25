import random
from timeit import repeat
from numba import njit

def monte_carlo_pi_without(nsamples):
    acc = 0
    for _ in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y **2 ) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

@njit
def monte_carlo_pi_with(nsamples):
    acc = 0
    for _ in range(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y **2 ) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples

t_without = min(repeat('monte_carlo_pi_without(1_000)', globals={"monte_carlo_pi_without": monte_carlo_pi_without}, number = 1_000))
t_with = min(repeat('monte_carlo_pi_with(1_000)', globals={"monte_carlo_pi_with": monte_carlo_pi_with}, number = 1_000))
print(f"Time without: {t_without:.3f}s")
print(f"Time with: {t_with:.3f}s")
print(f"Numba is {t_without / t_with:.2f} times faster")
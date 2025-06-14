print("100_numpy_solutions.py")
print("This file contains solutions to the numpy exercises.")
print("\n#1. Import the numpy package under the name np? (★☆☆)")
import numpy as np
print("\n#2. Print the numpy version and the configuration? (★☆☆)")
print(np.__version__)
print(np.show_config())
print("\n#3. Create a null vector of size 10? (★☆☆)")
a = np.zeros(10)
print(f"{a=}")
print("\n#4. How to find the memory size of any array? (★☆☆)")
print(f"{a.nbytes=}")
print("\n#5. How to get the documentation of the numpy add function from the command line? (★☆☆)")
print(np.info(np.add))
print("\n#6. Create a null vector of size 10 but the fifth value which is 1? (★☆☆)")
a[4] = 1
print(f"{a=}")
print("\n#7. Create a vector with values ranging from 10 to 49? (★☆☆)")
a = np.arange(10, 50)
print(f"{a=}")
print("\n#8. Reverse a vector (first element becomes last)? (★☆☆)")
a = a[::-1]
print(f"{a=}")
print("\n#9. Create a 3x3 matrix with values ranging from 0 to 8? (★☆☆)")
a = np.arange(9).reshape(3, 3)
print(f"{a=}")
print("\n#10. Find indices of non-zero elements from [1, 2, 0, 0, 4, 0]? (★☆☆)")
a = np.array([1, 2, 0, 0, 4, 0])
print(f"{np.nonzero(a)=}")
print("\n#11. Create a 3x3 identity matrix? (★☆☆)")
a = np.eye(3)
print(f"{a=}")
a = np.identity(3)
print(f"{a=}")
print("\n#12. Create a 3x3x3 array with random values? (★☆☆)")
a = np.random.random((3, 3, 3))
print(f"{a=}")
print("\n#13. Create a 10x10 array with random values and find the minimum and maximum values? (★☆☆)")
a = np.random.random((10, 10))
print(f"{a=}")
print(f"{np.min(a)=}")
print(f"{np.max(a)=}")
print("\n#14. Create a random vector of size 30 and find the mean value? (★☆☆)")
a = np.random.random(30)
print(f"{a=}")
print(f"{np.mean(a)=}")
print("\n#15. Create a 2d array with 1 on the border and 0 inside? (★☆☆)")
a = np.ones((5, 5))
a[1:-1, 1:-1] = 0
print(f"{a=}")
print("\n#16. How to add a border (filled with 0's) around an existing array? (★☆☆)")

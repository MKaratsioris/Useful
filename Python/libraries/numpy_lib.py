""" import numpy as np
import matplotlib.pyplot as plt """

'''
a = np.array([1, 2, 3], dtype='int64')
print(f"{a=}")
print(f"{a.ndim=}")
print(f"{a.shape=}")
print(f"{a.dtype=}")
print(f"{a.size=} elements")
print(f"{a.itemsize=} byte(s) / element")
print(f"{a.nbytes=} bytes")

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]], dtype='int8')
print(f"{a=}")
print(f"{a.shape=}")
print(f"{(a[1, 5] - 3)=}")
print(f"{a[0, :]=}")
print(f"{a[:, 2]=}")

a = np.zeros((3, 3))
print(f"{a=}")
a = np.ones((4, 4))
print(f"{a=}")
a = np.identity(3)
print(f"{a=}")
a = np.full((2, 2), 100)
print(f"{a=}")
a = np.linspace(0, 10, 100)
a = np.arange(0, 10, 0.02)

a = np.random.rand(3, 3)
print(f"{a=}")
a = np.random.randint(7, size=(3, 3))
print(f"{a=}")
a = np.random.randint(1, 11, size=(3, 3))
print(f"{a=}")

a = np.ones((5, 5))
a[1:-1, 1:-1] = 0
a[2, 2] = 9
print(f"{a=}")

a = np.ones((2, 3))
b = np.full((3, 2), 2)
c = np.matmul(a, b)
d = np.identity(3)
print(f"{a=}")
print(f"{b=}")
print(f"{c=}")
print(f"{np.linalg.det(d)=}")

stats = np.array([[1, 2, 3], [4, 5, 6]])
print(f"{np.min(stats)=}")
print(f"{np.min(stats, axis=1)=}")
print(f"{np.max(stats)=}")
print(f"{np.sum(stats)=}")
print(f"{np.sum(stats, axis=0)=}")

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"{before=}")
after = before.reshape((8, 1))
print(f"{after=}")
after = before.reshape((4, 2))
print(f"{after=}")

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
v3 = np.vstack([v1, v2])
print(f"{v3=}")
a = np.zeros((4, 3))
b = np.ones((4, 4))
c = np.hstack([a, b])
print(f"{c=}")

data1 = np.genfromtxt('numpy_data.txt', delimiter=',')
print(f"{data1=}")
data2 = data1.astype('int32')
print(f"{data2=}")
print(f"{data2[(data2 < 11) | (data2 > 20)]=}")
print(f"{(data2 > 25).any(axis=0)=}")
print(f"{(data2 > 25).any(axis=1)=}")
print(f"{(data2 > 25).all(axis=0)=}")
print(f"{(data2 > 25).all(axis=1)=}")
print(f"{((data2 > 15) & (data2 < 25))=}")
print(f"{((data2 > 15) & (data2 < 25))=}")
print(f"{((data2 > 15) & (data2 < 25))=}")
print(f"{((data2 > 15) & (data2 < 25))=}")
print(f"{~((data2 > 15) & (data2 < 25))=}")

a = np.array([num for num in range(1, 31)])
a = a.reshape((6, 5))
print(f"{a=}")
b = a[2:4, :2]
print(f"{b=}")
c = a[[0, 1, 2, 3], [1, 2, 3, 4]]
print(f"{c=}")
d = a[[0, 4, 5], 3:]
print(f"{d=}")

x = np.linspace(0, 10, 10_001)
print(f"{x=}")
y = np.exp(-x / 10) * np.sin(x)
print(f"{y=}")
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Damped Sine Wave")
plt.grid(True)
plt.show()

x = np.linspace(0, 10, 10_001)
print(f"{x=}")
y = np.exp(-x / 10) * np.sin(x)
print(f"{y=}")
y_depr = y[(x >= 4) & (x <= 7)]
print(f"{y_depr=}")
print(f"{np.mean(y_depr)=}")
print(f"{np.std(y_depr)=}")
print(f"{np.percentile(y_depr, 80)=}")

x = np.linspace(0, 10, 10_001)
y = np.exp(-x / 10) * np.sin(x)
dydx = np.gradient(y, x)
plt.plot(x, dydx)
plt.xlabel("x")
plt.ylabel("dydx")
plt.title("Damped Sine Wave Gradient")
plt.grid(True)
plt.show()

x = np.linspace(0, 10, 10_001)
y = np.exp(-x / 10) * np.sin(x)
dydx = np.gradient(y, x)
dydx_0 = x[1:][dydx[1:] * dydx[:-1] < 0]
print(f"{dydx_0=}")

nums = np.arange(0, 10_001, 1)
nums = nums[(nums % 4 != 0) * (nums % 7 != 0)]#[:10]
print(f"{nums=}")
s = np.sum(nums)
print(f"{s=}")
'''

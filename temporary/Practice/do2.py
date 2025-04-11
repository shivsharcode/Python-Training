# a = set([1, 2, 3])
# b = set([2, 3, 4])
# c = a.intersection(b)
# print(c.issubset(a))
import numpy as np

a = np.array([[4, 3], [4, 6]])
b = np.array([[1, 2], [4, 5]])
c = np.sum(a + b)

print(c)

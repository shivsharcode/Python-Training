import numpy as np


# 1D array
arr1 = np.array([1, 2, 3, 5])
# 2D array
arr2 = np.array([ [1, 2], [3, 5] ])

# printing the output
print(arr1)
print(arr2)


# Creating zeros matrix/array
zerosArr = np.zeros((2,3))
print(zerosArr)

# Creating ones array
onesArr = np.ones((3,3))
print(onesArr)

# Creating an array of sequence
seqArr = np.arange(10)
print(seqArr)

linspaceArr = np.linspace(0,1,4)
print(linspaceArr)

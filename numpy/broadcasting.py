import numpy as np

# when the column or row shape numbers between two arrays matches, or one of the numbers is 1
# then we can broadcast these two arrays

# same dimension broadcasting

array1 = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])

array2 = np.array([[1], [2], [3], [4]])

array3 = np.array([[1], [2], [3], [4], [5]])

print("array dimensions")
print(array1.ndim)
print(array2.ndim)

print(array1 * array2) # brodcastable

try:
    print(array1 * array3) # not broadcastable
except: ValueError

print("broadcastable shape")
print(array1.shape)
print(array2.shape)

print("non broadcastable shape")
print(array1.shape)
print(array3.shape)

# inter dimensional broadcasting

threeDimArray = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                        [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

twoDimArray = np.array([[1], [2], [3]])

print("array dimensions")
print(threeDimArray.shape)
print(twoDimArray.shape)

print(threeDimArray * twoDimArray)

# EXERCISE: Multiplication table

arrayOne = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
arrayTwo = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10],])

print(arrayOne * arrayTwo) 
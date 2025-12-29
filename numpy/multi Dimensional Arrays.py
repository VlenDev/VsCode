import numpy as np

# zero dimensional array
zeroArray = np.array(1)
print(zeroArray.ndim)
print(zeroArray.shape)
print(zeroArray)

# one dimensional array
oneArray = np.array([1, 2, 3])
print(oneArray.ndim)
print(oneArray[2]) # 3
print(oneArray.shape)
print(oneArray)

# two dimensional array
twoArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(twoArray.ndim)
print(twoArray[1, 0]) # 4
print(twoArray.shape)
print(twoArray)

# three dimensional array
threeArray = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                        [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                        [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])
print(threeArray.ndim)
print(threeArray[2, 1, 1]) # 23
print(threeArray.shape)
print(threeArray)

number = threeArray[0, 1, 2] + threeArray[2, 1, 0] + threeArray[1, 0, 0]
print(number)
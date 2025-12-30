import numpy as np

#Scalar arithmetic

array = np.array([1, 2, 3])
print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

# vectorized math functions

vArray = np.array([1.4890,  2.3893, 3.4390])
print(np.sqrt(vArray))
print(np.round(vArray))
print(np.floor(vArray))
print(np.ceil(vArray))

# EXERCISE

radii = np.array([1, 2, 3])
print(np.pi * radii ** 2)

# Element wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([3, 4, 5])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)
print(array1 / array2)
print(array1 ** array2)

#comparison operators

scores = np.array([91, 55, 100, 73, 82, 64])
print(scores == 100)
print(scores >= 60)
print(scores < 60)

scores[scores < 60] = 0
print(scores)
import numpy as np

array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])
# slicing: array[start:end:step]

print(array[0:3]) # prints section from index 0 to index 3 (excluding index 3)
print(array[0:4:2]) # prints section from index 0 to 4, skipping every second line
print(array[::-1]) # prints array in reverse order
print(array[:, 0]) # prints only the first column
print(array[:, 0:3]) # prints a section from the first column to the third one
print(array[0:2, 0:2]) # prints the top left quadrant
print(array[0:2, 2:]) # prints the top left quadrant
print(array[2:, 0:2]) # prints the bottom left quadrant
print(array[2:, 2:]) # prints the bottom right quadrant
print(array[:,:]) # prints array, since : means every column, or row
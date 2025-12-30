import numpy as np

array = np.array([[21, 17, 23, 16, 30, 55, 21, 18],
                  [76, 99, 29, 31, 17, 16, 19, 20]])

teenagers = array[array < 18]
print(teenagers)

adults = array[(array >= 18) & (array < 65)]
print(adults)

seniors = array[array > 65]
print(seniors)

evens = array[array % 2 == 0]
print(evens)

odds = array[array % 2 != 0]
print(odds)

adults = np.where(array >= 18, array, 0)
print(adults)
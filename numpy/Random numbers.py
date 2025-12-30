import numpy as np

# Random Integers

rng = np.random.default_rng(seed=1)

print(rng.integers(1, 11, (3, 2)))

# Random floating point numbers

np.random.seed(1)

print(np.random.uniform(-1, 1, (3, 2)))

# Shuffling

array = np.array([1, 2, 3, 4, 5])
rng.shuffle(array)
print(array)

# Random choice

fruits = np.array(["apple", "orange", "banana", "strawberry", "coconut", "pineapple"])
fruit = rng.choice(fruits, (3, 3))
print(fruit)
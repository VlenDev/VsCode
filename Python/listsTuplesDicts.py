# List Manipulation Practice
numbers = [1, 2, 3, 4, 5]
numbers[0] = 2
numbers.append(6)
numbers.insert(6, 7)
numbers[0] = 1
numbers.remove(7)
numbers.pop(5)
print(numbers)
print(len(numbers))
print(numbers.index(1))
# output: [1, 2, 3, 4, 5]

#tuple manipulation practice
tuple = (1, 2, 3, 4, 5)
print(tuple)
x = len(tuple)
print(x)
# output: (1, 2, 3, 4, 5) 5

# Dictionary Manipulation Practice
dictionary = {"name": "Vlen", "age": 15, "village": "Rahovec", "country": "Kosovo"}
dictionary["age"] = 14
print(dictionary["age"])
dictionary["city"]  = "Prizren"
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(len(dictionary))
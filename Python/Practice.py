#variable and data type practice
stringVar = "Hello, World!"
intVar = 42
floatVar = 3.14
boolVar = True
print(type(stringVar))
print(type(intVar))
print(type(floatVar))
print(type(boolVar))

print(stringVar)
print(intVar)
print(floatVar)
print(boolVar)
# output: <class 'str'> <class 'int'> <class 'float'> <class 'bool'>

# operators practice
x = 10
y = 5
print(x + y)  # addition
print(x - y)  # subtraction
print(x * y)  # multiplication
print(x / y)  # division
print(x % y)  # modulus
print(x ** y) # exponentiation
print(x // y) # floor division
# output: 15 5 50 2.0 0 100000

# conditional statements practice
a = 10
b = 20
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
elif a == 10 and b == 10:
    print("Both a and b are 10")
elif a == 10 or b == 10:
    print("Either a or b is 10")
elif not a == 10:
    print("a is not 10")
else:
    print("a is greater than b")

# loop practice

# for loop
for i in range(5):
    print(i)

# while loop
count = 0
while count < 5:
    print(count)
    count = count + 1

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
dictionary = {"name": "Vlen", "age": 15, "city": "Rahovec", "country": "Kosovo"}
dictionary["age"] = 14
print(dictionary["age"])
dictionary["city"]  = "Prizren"
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(len(dictionary))

# function practice
def greet(name): # creating the function "greet" and adding the "name" parameter
    print(f"Hello {name}!") # printing a greeting along with the name parameter
greet("Vlen") # calling the function and adding the parameter "Vlen"

def addition(a, b): # creating an addition function to add values a and b
    return a + b # returning the addition of values a and b
result = addition(6 , 7) # asssigning the returning values of the addition function to the variable "result"
print(result) # printing the result                             

def defaultGreetings(name="Guest", pronoun=""): # creating function including deafult parameters
    print(f"Hello {pronoun} {name}!") # printing the greeting with the "name" and "pronoun" parameter
defaultGreetings("Vlen", "Mr.") #prints "Vlen" with the pronouns Mr.
defaultGreetings() # prints "Guest" which is the default value for variable "name"
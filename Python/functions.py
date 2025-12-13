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
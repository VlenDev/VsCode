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
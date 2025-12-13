# list / dictionary comprehension
listCompReg = [x for x in range(5)]
listCompSqr = [x * x for x in range(5)]
listCompOdd = [x for x in range(5) if x % 2 == 1]
listCompEvn = [x for x in range(5) if x % 2 == 0]
dictCompReg = {x: x for x in range(5)}
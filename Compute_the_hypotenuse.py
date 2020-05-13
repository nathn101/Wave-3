import math
def hypotenuse(a, b):
    hyp = math.sqrt((a ** 2) + (b ** 2))
    print("The hypotenuse is: " + str(hyp))

a = float(input("Enter first leg here: "))
b = float(input("Enter second leg here: "))
hypotenuse(a, b)
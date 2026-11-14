#Amir Abdollah Abdollahi
import math

def hypot(a, b):
    return math.sqrt(a * a + b * b)


x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print("Hypotenuse =", hypot(x, y))
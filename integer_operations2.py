a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

total = a + b
diff = a - b
prod = a * b
quot = a // b
ram = a % b
exp = a ** b

print(str(a) + " + " + str(b) + " = " + str(total))
print(str(a) + " - " + str(b) + " = " + str(diff))
print(str(a) + " * " + str(b) + " = " + str(prod))
print(str(a) + " // " + str(b) + " = " + str(quot))
print(str(a) + " % " + str(b) + " = " + str(ram))
print(str(a) + " ** " + str(b) + " = " + str(exp))
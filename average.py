import random

n = 10
a = [random.randint(0, 100) for i in range(n)]

total =0.0
for v in a:
    total += v
average = total / len(a)

print(average)
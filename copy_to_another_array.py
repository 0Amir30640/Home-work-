import random

n = 10
a = [random.randint(0, 100) for i in range(n)]

b = []
for v in a:
    b += [v]

print(b)
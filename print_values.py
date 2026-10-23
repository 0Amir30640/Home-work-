import random

n = 10

a = [random.uniform(0, 10) for i in range(n)]

for v in a:
    print(v)

maximum = max(a)

average = float(sum(a)) / len(a)

b = a[:]

a = a[::-1]
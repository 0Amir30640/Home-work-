import random

n = 10
a = [random.randint(0, 100) for i in range(n)]
print(a)
maximum = a[0]
for v in a[1:]:
    if (v > maximum):
        maximum = v

print(maximum)
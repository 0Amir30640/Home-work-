# Amir Abdollah Abdollahi
import random
import matplotlib.pyplot as plt
x = 0
y = 0
X = []
Y = []
for i in range(100000):
    r = random.random()
    if r < 0.40:
        a = 0.31*x - 0.53*y + 0.89
        b = -0.46*x - 0.29*y + 1.04
    elif r < 0.55:
        a = 0.31*x - 0.08*y + 0.22
        b = 0.15*x - 0.45*y + 0.34
    else:
        a = 0.55*y + 0.01
        b = 0.69*x - 0.20*y + 0.38
    x = a
    y = b
    if i > 100:
        X.append(x)
        Y.append(y)
plt.scatter(X, Y, s=0.1)
plt.title("Coral Reef")
plt.show()
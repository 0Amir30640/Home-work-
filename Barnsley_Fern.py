# Amir Abdollah Abdollahi
import random
import matplotlib.pyplot as plt
x, y = 0, 0
X, Y = [], []
for i in range(50000):
    r = random.random()
    if r < 0.01:
        x, y = 0, 0.16*y
    elif r < 0.86:
        x, y = 0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6

    elif r < 0.93:
        x, y = 0.20*x - 0.26*y, 0.23*x + 0.22*y + 1.6

    else:
        x, y = -0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44

    X.append(x)
    Y.append(y)

plt.scatter(X, Y, s=0.1, color="green")
plt.axis("off")
plt.show()
from matplotlib import pyplot as plt
from math import exp
from numpy import linspace

def Euler(n, a, b):
    xi = 0
    yi = 1
    y = [yi]
    x = [xi]
    h = (b-a)/n

    for _ in range(1, n+1):
        xi1 = xi + h
        yi1 = yi + h * yi
        xi = xi1
        yi = yi1
        x.append(xi)
        y.append(yi1)

    plt.plot(x, y, label="Euler"+str(n))

for m in range(1, 5):
    Euler(m, 0, 1)

xv = linspace(0, 1, 100)
yv = [exp(x) for x in xv]
plt.plot(xv, yv, label="Solution exacte")

plt.legend()
plt.show()
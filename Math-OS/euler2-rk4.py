from matplotlib import pyplot as plt
from math import exp
from numpy import linspace
import time

def f(x, y):
    return y

def rk4(n, a, b):
    xi = 0
    yi = 1
    y = [yi]
    x = [xi]
    h = (b-a)/n

    for _ in range(1, n+1):
        k1 = f(xi, yi)
        k2 = f(xi, yi + ((b-a)/(2**n)) * k1)
        k3 = f(xi, yi + ((b-a)/(2*n)) * k2)
        k4 = f(xi, yi + h * k3)
        pente = (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)
        xi1 = xi + h
        yi1 = yi + h * pente
        xi = xi1
        yi = yi1
        x.append(xi)
        y.append(yi1)

    plt.plot(x, y, label="rk4 "+str(n))

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

    plt.plot(x, y, label="EULER "+str(n))

def temps_rk4(m):
    start = time.now()
    rk4(m, 0, 1)
    elapsed = time.now() - start
    return elapsed

for m in range(1, 5):
    rk4(m, 0, 1)
for m in range(1, 5):
    Euler(m, 0, 1)

xv = linspace(0, 1, 100)
yv = [exp(x) for x in xv]
plt.plot(xv, yv, label="Solution exacte")

plt.legend()
plt.show()
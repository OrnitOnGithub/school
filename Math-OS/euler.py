from math import sqrt
from matplotlib import pyplot as plt

h = []

def f(x):
    return sqrt(x**2 + 2)

def Euler(a, b, n, x0, y0):
    h = (b-a)/n
    x = x0
    y = y0
    x_liste = []
    y_liste = []
    for i in range(1, n+1):
        x2 = x + h
        y2 = y + h * f(x)
        x = x2
        y = y2
        x_liste.append(x)
        y_liste.append(y)
    plt.plot(x_liste, y_liste)
    print(x_liste, y_liste)
    #return x_liste, y_liste

Euler(0, 1, 3, 0, 1)


#plt.plot(x, y)
plt.show()
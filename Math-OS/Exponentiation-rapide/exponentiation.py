from time import *
from matplotlib import pyplot as plt

def exprapide(x, n):
    a = 1

    while n > 0:
        if n % 2 == 1:
            a *= x

        x *= x 
        n //=2

    return a

def exp(x, n):
    a = 1
    for i in range(n):
        a *=x
    return a


def exprapide_rapidité(x,n):
    start = time()
    exprapide(x,n)
    end = time()
    return end - start

def exp_rapidité(x,n):
    start = time()
    exp(x,n)
    end = time()
    return end - start

a, n = 3, 12000
y, x = [exprapide_rapidité(a,x) for x in range(n)], [x for x in range(n)]
y2, x2 = [exp_rapidité(a,x) for x in range(n)], [x for x in range(n)]


plt.plot(x,y, label="exp rapide")
plt.plot(x2,y2, label="exp normale")
plt.ylabel("n")
plt.xlabel("time")
plt.show()
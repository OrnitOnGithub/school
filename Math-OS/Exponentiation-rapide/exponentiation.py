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


a, n = 5, 100 # a^n
y, y2 = [exprapide_rapidité(a,x) for x in range(n)], [exp_rapidité(a,x) for x in range(n)]

diff = [(y2[x] - y[x]) for x in range(len(y))]

# Les graphes des vitesses des deux fonctions
plt.plot(y, label="exp rapide")
plt.plot(y2, label="exp normale")

# Le graphe de la différence de temps entre les deux
plt.plot(diff, label="différence")

plt.ylabel("temps")
plt.xlabel("n")
plt.show()



from time import *
from matplotlib import pyplot as plt

def exprapide(base, exponent):
    resultat_final = 1

    while exponent > 0:
        if exponent % 2 == 1:
            resultat_final *= base

        base *= base
        exponent //=2

    return resultat_final

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


a, n = 5, 10000 # a^n
y, y2 = [exprapide_rapidité(a,x) for x in range(n)], [exp_rapidité(a,x) for x in range(n)]

diff = [(y2[x] - y[x]) for x in range(len(y))]

# Les graphes des vitesses des deux fonctions
plt.plot(y, label="exp rapide")
plt.plot(y2, label="exp normale")

# Le graphe de la différence de temps entre les deux
plt.plot(diff, label="différence")

plt.ylabel("temps")
plt.xlabel("n")
plt.legend()
plt.show()



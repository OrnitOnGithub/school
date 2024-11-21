from matplotlib import pyplot as plt
import math

def f(x):  return -x**2 +2
def fd(x): return x**2

def secante(a=-2, b=-1, epochs=20):
    for _ in range(epochs): a = a - (b - a)/(f(b)-f(a)) * f(a)
    return a

def dichotomie(interval_start, interval_end, epochs=10):
    milieu = 0
    for _ in range(epochs):
        milieu = (interval_start + interval_end) / 2
        print(milieu)
        if f(milieu) > 0:
            interval_end = milieu
        else: 
            interval_start = milieu
        print(milieu)
    return interval_start

def tangente(a=1, b=2, epochs=20):
    pass

def newton(a=1, b=2, epochs=20):
    a = 2
    for i in range(epochs):
        a = a - f(a)/fd(a)
    return a


# print(dichotomie(1, 2, 100))
# answer = math.sqrt(2)
# print(answer)
# 
# x = [(-math.log10(abs(answer - dichotomie(1, 2, x)))) for x in range(100)]
# 
# plt.plot(x)
# plt.show()

print(secante())

answer = math.sqrt(2)
print(answer)
x=100
print(answer - secante(1, 2, x))

# y = [(-math.log10(abs(answer - secante(1, 2, x)))) for x in range(100)]
y = []
for x in range(100):
    y.append(-math.log10(abs(answer - secante(1, 2, x))))
plt.plot(y)
plt.show()

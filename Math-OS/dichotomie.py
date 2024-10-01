from matplotlib import pyplot as plt
import math

def f(x):
    return x**2 -2

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

print(dichotomie(1, 2, 100))
answer = math.sqrt(2)
print(answer)

x = [(-math.log10(abs(answer - dichotomie(1, 2, x)))) for x in range(100)]

plt.plot(x)
plt.show()

import math
from matplotlib import pyplot as plt
import time

def f(x):
    return math.exp(x)

def rectangles(n, b, a):
    answer = 0
    for k in range(n):
        answer += (b-a)/n * f(a+k * ((b-a)/n))
    return answer

def simpson(n, a, b):
    pass
print(rectangles(4, 1, 0))

iterations = 3

correct = []
times = []

for x in range(iterations):
    #-math.log10(abs(answer - secante(1, 2, x))))
    correct.append(-math.log10(abs((f(1)-1)-rectangles(x, 1, 0))))

for x in range(iterations):
    start = time.time()
    _ = rectangles(10 ** x, 1, 0)
    end = time.time()
    elapsed = end - start
    times.append(elapsed)

#print(correct)

plt.plot(times, label="Rectangle")
plt.legend()
plt.ylabel("Nombre de décimaux corrects")
plt.xlabel("n")
plt.show()
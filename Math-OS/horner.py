l = [3, -1, 1, -2, 3];

def naive(l, x):
    s = 0;
    len_l = len(l);
    for i in range(len_l):
        s += l[i] * x**i;
    return s;

def horner(l, x):
    s = 0;
    len_l = len(l);
    for i in range(len_l):
        s = s*x + l[len_l-i-1];
        # print(s);
    return s;

print(naive(l, 2));
print(horner(l, 2));

from matplotlib import pyplot as plt
import time
import random

time_average_iterations = 10

def time_naive(l):
    result = 0
    for _ in range(time_average_iterations):
        x = random.randint(-9, 9)
        start = time.time()
        _ = naive(l, x)
        end = time.time()
        result += end - start
    return result / time_average_iterations

def time_horner(l):
    result = 0
    for _ in range(time_average_iterations):
        x = random.randint(-9, 9)
        start = time.time()
        _ = horner(l, x)
        end = time.time()
        result += end - start
    return result / time_average_iterations

print(time_naive(l))
print(time_horner(l))

def polynome_1_n(n):
    s = []
    for _ in range(n):
        s.append(1)
    return s 

print(polynome_1_n(12))
epochs = 1000
times_naive = [time_naive(polynome_1_n(x)) for x in range(epochs)]
times_horner = [time_horner(polynome_1_n(x)) for x in range(epochs)]

print(times_horner)


plt.plot(times_naive, label="Simple")
plt.plot(times_horner, label="Horner")
plt.legend()
plt.ylabel("Temps d'execution (s)")
plt.xlabel("Degré du polynome")
plt.show()

import math
import random
def f(x): return (-(x**3) + 4*(x**2) -3*x)
precision = 1000000
a = 1
b = 3
max = f((4+math.sqrt(7))/3)
points_x = [a + random.random() * (b-a) for _ in range(precision)]
points_y = [random.random() * (max) for _ in range(precision)]
total = precision
below = 0
for i in range(precision):
 x = points_x[i]
 y = points_y[i]
 if y < f(x):
   below += 1 # below
area = (below/total) * ((b-a) * (max))
print(area)

"""
from matplotlib import pyplot as plt
plt.plot()
plt.show()
"""
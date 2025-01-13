from matplotlib import pyplot as plt
import numpy as np

def f(x):
    return (-(5/12)*(x**3) - (2/3)*(x**2) + (11/12)*(x) + (19/6))

data_x = [1, -1,  2, -2]
data_y = [3,  2, -1,  2]
x_list = np.linspace(-2, 2, 100)
y_list = []

for x in x_list:
    y_list.append(f(x))

plt.plot(x_list, y_list, label="Lagrange")
plt.scatter(data_x, data_y, color="red", label="Points")
plt.legend()
plt.show()
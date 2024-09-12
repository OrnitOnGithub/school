def pgdc(x, y):
    while y != 0: y, x = x % y, y
    return x

print(pgdc(220, 700))

# Programme d'avant, plus clair:
"""
def pgdc(x, y):
    previous = 1
    while True:
        z = x % y
        x = y
        y = z
        if z == 0:
            return previous
        previous = z
"""

"""
Méthode d'Euclide :
782 = 3*221 + 119
221 = 1*119 + 102
119 = 1*102 + 17
102 = 6*17 + 0
"""

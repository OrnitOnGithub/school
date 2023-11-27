def heron (A, i) :
    """
    Nombre A
    Tu fais un rectangle d'aire A
    Largeur = nombre cherché
    Puis on fait la moyenne de longeur et largeur
    Cette moyenne c'est la nouvelle largeur
    """
    largeur = A
    longueur = largeur / A

    while (longueur - largeur < 10**(-i)): # Tant que longueur - largeur < 10^-n
        longueur = (largeur + longueur) / 2
        largeur = A / longueur
        print(largeur)
    
    return largeur





from matplotlib import pyplot as plt


x_values = list(range(1, 100))

y_values = [heron(x, 5) for x in x_values]

plt.plot(x_values, y_values)
plt.xlabel('x')
plt.ylabel('Square root of x')
plt.title('Square Root Function')
plt.show()

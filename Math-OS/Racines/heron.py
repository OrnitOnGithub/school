def heron (A, i) :
    """
    Nombre A
    Tu fais un rectangle d'aire A
    Largeur = nombre cherché
    Puis on fait la moyenne de longeur et largeur
    Cette moyenne c'est la nouvelle largeur
    """
    print(f"x: {A}")
    largeur = A
    longueur = largeur / A


    for _ in range(i):
        print(f"longueur - largeur = {longueur - largeur}")
        longueur = (largeur + longueur) / 2
        largeur = A / longueur
        print(f"largeur: {largeur} longueur: {longueur}")

        
    return largeur


from matplotlib import pyplot as plt

def fonction_racine():
    x_values = list(range(2, 100))
    y_values = [heron(x, 100) for x in x_values]

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('Racine de x')
    plt.title('Fonction Racine')
    plt.show()


# JSP comment ca marche tout ca

def heron2 (A, i) :
    """
    Nombre A
    Tu fais un rectangle d'aire A
    Largeur = nombre cherché
    Puis on fait la moyenne de longeur et largeur
    Cette moyenne c'est la nouvelle largeur
    """
    print(f"x: {A}")
    largeur = A
    longueur = largeur / A


    for _ in range(i):
        print(f"longueur - largeur = {longueur - largeur}")
        longueur = (largeur + longueur) / 2
        largeur = A / longueur
        print(f"largeur: {largeur} longueur: {longueur}")

        
    return longueur - largeur

def précision(a):
    x_values = list(range(1, 10))
    y_values = [heron2(a, x) for x in x_values]

    plt.plot(x_values, y_values)
    plt.xlabel('x')
    plt.ylabel('Racine de x')
    plt.title('Fonction Racine')
    plt.show()


précision(13)
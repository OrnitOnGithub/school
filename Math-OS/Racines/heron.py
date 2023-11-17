# Nombre A
# Tu fais un rectangle d'aire A
# Largeur = nombre cherché
# Puis on fait la moyenne de longeur et largeur
# Cette moyenne c'est la nouvelle largeur

A = int(input("Entrez le chifre: \n"))
i = int(input("Entrez le niveau de profondeur: \n"))
largeur = A
longueur = largeur / A

for _x in range(i):
    longueur = (largeur + longueur) / 2
    largeur = A / longueur
    print(largeur)
# Chiffrement affine

## Congruences

Voici un script Python (qui marche sur les calculatrices de l'école) qui peut résourde un problème comme `6x ≡ 5 [26]`
```python
# Warning! This program assumes 0 < b < c
# Convenient I know.
print("ax ≡ b [c]")

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

x = 0
while True:
    if (a * x) % c == b:
        break
    x += 1

print(f"The solution for {a}x ≡ {b} [{c}] is: {x}")
print(f"a ≡ {x} [{c}]")
```
## Exemple de résolution
(pas du tout celui de la prof)

### Données
```
A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z
0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
```
```
Message = SEPGVB

E = E
J = N (J remplacé par N)
```
### Résolution
```
soit f(x) = ax + b    avec a,b appartiennent à [0;15]
soit "=" un remplacement pour le signe congru

on a:
E <=> 4
J <=> 9
N <=> 13

on a:
4a + b  = 4  [26]
9a + b  = 13 [26]

mais puisqu'on aura besoin de la fonction réciproque, à la place on peut résourde:
4a  + b = 4 [26]
13a + b = 9 [26]

b = 4 - 4a [26]
13a + (4 - 4a) = 0 [26]

donc
9a   = 5   [26]
3*9a = 3*5 [26]
27a  = 15  [26]
a    = 15  [16]

b =  4  - 4*15 [26]
b = -56        [26]
b = -56 + 3*26 [26]
b =  22        [26]

a = 15
b = 22

f⁻¹(x) = 15x + 22

```

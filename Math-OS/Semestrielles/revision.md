# Chiffrement et congruences

## Exemple de résolution

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
a    = 15  [26]

b =  4  - 4*15 [26]
b = -56        [26]
b = -56 + 3*26 [26]
b =  22        [26]

a = 15
b = 22

f⁻¹(x) = 15x + 22

```

# Méthode de Héron

## Exemple

Calculons $\sqrt{7}$

```
L0 = 7                           et  l0 = 1

L1 = (7 + 1) / 2 = 4             et  l1 = 7 / 4

L2 = (4 + (7 / 4)) / 2 = 23 / 8  et  l2 = 7 / (23 / 8)

[...]
```


## Rapidité de calcul:

on va admettre que pour tout n $\in$ $\mathbb{N}, a_n \geqslant \sqrt{A}$


$$
\begin{aligned}
\forall n \in N, a_{n+1}-\sqrt{A} & =\frac{1}{2}\left(a_n+\frac{A}{a_n}\right)-\sqrt{A} \\
& =\frac{1}{2}\left(\frac{a_n^2}{a_n}+\frac{A}{a_n}-\frac{2 \sqrt{A} a_n}{a_n}\right) \\
& =\frac{1}{2}\left(\frac{a_n^2-2 \sqrt{A} a_n+A}{a_n}\right) \\
& =\frac{1}{2} *\frac{\left(a_n-\sqrt{A}\right)^2}{a_n} \\
& \leqslant \frac{\left(a_n-\sqrt{A}\right)^2}{2 \sqrt{A}}
\end{aligned}
$$

Important à se rappeler:

$\forall \  n \in N, \ a_{n+1}-\sqrt{A} =\frac{1}{2}\left(a_n+\frac{A}{a_n}\right)-\sqrt{A}$

le reste c'est de la factorisation

# Cinématique

## Changer de référenciel

### Cartésien -> polaire
```
r = √(x² + y²)

0 = tan⁻¹(y/x)
```
### Polaire -> cartésien
```
x = r * cos(a)

y = r * sin(a)
```

## Vitesse linéaire <\-\> Vitesse angulaire
```
w = v/r

v = w*r

w = vitesse angulaire (rad/s)
v = vitesse linéaire  (m/s)
r = rayon             (m)
```


## Accélération && force centripète
```
ac = v²/r

fc = m * v²/r
    (m * ac)
```
## Accélération angulaire dans un MCUA
```
α = w/t
```
## Angle en fonction de vitesse angulaire initiale et accélération angulaire

```
θ = 1/2*αt² + wi*t

θ = angle parcouru              (rad)
α = accélération angulaire      (rad/s²)
wi = vitesse angulaire initiale (rad/s)
t = temps                       (s)
```

## vitesse angulaire en fonction de vitesse angulaire initiale et accélération angulaire

```
w = αt + wi

w = vitesse angulaire           (rad/s)
α = accélération angulaire      (rad/s²)
wi = vitesse angulaire initiale (rad/s)
t = temps                       (s)
```

## Toutes les equations

```
w = v/r
v = w*r

ac = v²/r
fc = m * v²/r

α = w/t

0 = ½αt² + wi*t
w = αt + wi

-----------------------------------

r = rayon                    (m)
v = vitesse                  (m/s)
w = vitesse angulaire        (rad/s)
α = accélération angulaire   (rad/s²)
ac = accélération centripète (m/s²)
```
Version réduite:
```
w = v/r

ac = v² / r

a = w / t

0 = ½αt² + wi*t
w = αt + wi
```

# Dynamique

## Centre de masse

```
        M1 * X1 + M2 * X2
rx = -------------------
             M1 + M2

r = vecteur position
M = masse
X = position sur axe X
```

## Types de collisions

- Elastique
  - L'énergie cinétique initiale = finale
- Inelastique
  - Ecin initiale > Ecin finale
- Explosive
  - Quand Ecin initiale < Ecin finale
- Parfaitement Inelastique
  - L'énergie objet a et b fusionnent

## Propulsion

```
Fp = deltaP / deltaT

Fp = force propulsion
deltaP = P (quantité de mouvement) initial - final
```

## Impulsion

```
J = F * dT

J = dP

F = Force d'impact / temps

J = impulsion
F = Force constante
dT = delta T
dP = delta P = delta quantité de mouvement
```

## Système isolé masse variable

$$
F_{prop} = m_{1}\frac{dv_{1}}{dt} = v_{rel}\frac{dm_{2}}{dt}
$$

<br>

$F_{prop}$​ : Force de propulsion de la fusée.

$m_{1}$​ : Masse de la fusée (ou la masse du carburant consommé).

$dv_{1}/dt$ : C'est la variation de la vitesse (v1​) de la fusée par rapport au temps (t). Cela représente l'accélération de la fusée.

$v_{rel}$​ : Vitesse d'éjection des gaz (vitesse relative des gaz par rapport à la fusée).

$dm_{2}/dt$ : C'est la variation de la masse du carburant (m2m2​) par rapport au temps (tt). Cela représente le débit de carburant, c'est-à-dire la masse de carburant consommée par unité de temps.

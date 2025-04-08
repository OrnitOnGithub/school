A = [[1, 2, 1], [-1, 1, 2], [3, 1, -1]]
B = [[8], [3], [-3]]

def print_mat(x):
    for i in range(3):
        if i == 0:
            print(" /", end="")
        if i == 1:
            print("| ", end="")
        if i == 2:
            print(" \\", end="")
        for j in range(3):
            if x[i][j] > 0: print(" ", end="")
            print(x[i][j], "", end="")
        if i == 0:
            print("\\", end="")
        if i == 1:
            print(" |", end="")
        if i == 2:
            print("/", end="")

        print()


def triangle(A, B):
    pass

for x in range(3):
    A[x][0], A[x][1] = A[x][1], A[x][0]

def det(A, B):
    A, B= triangle(A, B)
    p = 1
    for i in range(len(A)):
        p*= A[i][i]
    return p

print_mat(A)


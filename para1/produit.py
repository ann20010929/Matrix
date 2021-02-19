# produit de deux matrices

def produit_matriciel(A, B):
    for i in range(len(A)):
        if i != 0:
            print()
        else:
            print('[ ', end='')
        for j in range(len(B[0])):
            mij = 0
            for p in range(len(A[0])):
                mij += A[i][p] * B[p][j]
            print(mij, end=' ')
    print(']')


# produit_matriciel(C, D)

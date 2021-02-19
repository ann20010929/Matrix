A = [[12, 7],
     [4, 5],
     [7, 8]]

B = [[5, 8, 1, 5],
     [6, 7, 3, 3]]

C=[[5, 8, 1, 5],
    [6, 7, 3, 3],
    [5, 8, 1, 5],
    [6, 7, 3, 3]]
D=[[1],
   [2],
   [0],
   [0]]

# produit des deux matrices

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


produit_matriciel(C, D)

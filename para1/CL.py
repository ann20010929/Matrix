# addition
def addition(A, B):
    for i in range(len(A)):
        if i != 0:
            print()
        else:
            print('[', end='')
        for j in range(len(A[0])):
            if i == len(A) - 1 and j == len((A[0])) - 1:
                print(A[i][j] + B[i][j], end=']')
            else:
                cij = A[i][j] + B[i][j]
                print(cij, end=' ')


addition(C, D)



def scalaire(coeff, A):
    for i in range(len(A)):
        if i != 0:
            print()
        else:
            print('[', end='')
        for j in range(len(A[0])):
            print(coeff * A[i][j], end=' ')
    print(']')


scalaire(coeff, A)

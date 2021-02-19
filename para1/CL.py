A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

B = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

coeff = 2

C = [[12, 7],
     [4, 5],
     [5, 8],
     [6, 7]]
D = [[1, 7],
     [3, 2],
     [19, 8],
     [6, 6]]


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


# def scalaire(coeff,A): #faut app the list comprehension
#     mij=((coeff*A[i][j] for j in range(len(A[0])))for i in range(len(A)))
#     print(mij)

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

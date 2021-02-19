M = [[5, 8, 1],
     [6, 7, 3],
     [2, 5, 9]]

n = 3  # pour I3


def In(n):
    L1 = [1]
    for k in range(n - 1):
        L1.append(0)
    print(L1)
    for k in range(1, n):
        L1[k - 1], L1[k] = 0, 1
        print(L1)


In(n)


def MIn(M, In):  # combiner deux matrices à une seule pour la méth du pivot de Gauss-Jordan
    # M[1:1]=In[0] #slicing bof ici
    for k in range(0, len(M)):
        M.insert(2 * k + 1, In[k])  # insert meth
        # print(M)

    for k in range(len(M)):
        print(*M[k], sep=' ', end='  ')
        if k % 2 == 1:
            print()




# diag(1,...,n)
# def Dn(n):

def addition_diag(A,B):
    C=[]
    for k in range(len(A)):
        cij=A[k][k]+B[k][k]
        C.append(cij)
        # print(cij)
    return C

# 1 mq M est inversible <-- pivot de Gauss
# 2 trouve M^-1 <-- pivot de Jordan

# valable matrice carrée <-- logique
import numpy as np


def forward_elimination(M):
    diag = len(M)
    for k in range(diag - 1):
        # print(M)
        for i in range(k + 1, len(M)):  # ligne
            if M[k][k] == 0:
                for cord in range(1, len(M)):
                    if M[cord][k] != 0:
                        M[[k, cord]] = M[[cord, k]]
                        break
            else:
                ratio = M[i][k] / M[k][k]
                for j in range(len(M[0])):  # colonne
                    M[i][j] -= ratio * M[k][j]

    return M

#pour la beauté
def diag_1(M): #on veut que tous les mkk soient = 1
    M = forward_elimination(M)
    for k in range(len(M)):
        if M[k][k] != 1.:
            ratio = 1 / M[k][k]
            for i in range(k, len(M)):  # ligne
                for j in range(len(M[0])):  # colonne
                    M[i][j] *= ratio
    return M

  
def Jordan(M):
    M = diag_1(M)
    for k in range(len(M)):  # =3 pour M3(K)
        for i in range(k, len(M)):  # ligne
            for j in range(len(M[0])):  # colonne
                if (i < 3 and j < 3) and i!=j and M[i][j] != 0:
                        jArr = np.full(len(MIn)-1, j)
                        iArr = np.arange(0, len(M))
                        zeroIndexArr = np.array(i)
                        new_iArr = np.setdiff1d(iArr, zeroIndexArr)

                        for c in range(len(jArr)):
                            mij = M[new_iArr[c]][jArr[c]]
                            if mij != 0:
                                ratioForLrow = -(M[i][j] / M[j][j])
                                M[i, :] = M[i, :] + ratioForLrow * M[j, :]
                                break
    return M


#si on veut avoir les i et j sous forme de (i,j)
def mij_cord(L1, L2): #par ex : L1=new_iArr et L2=jArr
    listOfCoordinates = list(zip(L1, L2))
    for cord in listOfCoordinates:
        print(cord) 

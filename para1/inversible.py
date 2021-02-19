# 1 mq M est inversible <-- pivot de Gauss
# 2 trouve M^-1 <-- pivot de Jordan

# valable matrice carrée
import numpy as np

M = np.array([[5, 8, 1],
              [6, 7, 3],
              [2, 5, 9]])
I3 = np.array([[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]])
MI3 = np.array([[5, 8, 1, 1, 0, 0],
                [6, 7, 1, 0, 1, 0],
                [2, 5, 9, 0, 0, 1]])


def max_index0(MI3):
    L = []
    for k in range(len(MI3)):
        L.append(MI3[k][0])
    Max = max(L)
    indexMax = L.index(Max)
    return Max, indexMax
# print(max_index0(MI3))

def permuter_etape1(MI3):
    Max, indexMax = max_index0(MI3)
    MI3[[indexMax, 0]] = MI3[[0, indexMax]]
    print(MI3)


permuter_etape1(MI3)

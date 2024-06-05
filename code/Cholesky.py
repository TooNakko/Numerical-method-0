import numpy as np
from math import *

def Cholesky(A,B):
    l11 = sqrt(A[0][0])
    l21 = A[0][1] / l11
    l22 = sqrt(A[1][1] - pow(l21,2))
    l31 = A[0][2] / l11
    l32 = (A[2][1] - l31 * l21) / l22
    l33 = sqrt(A[2][2] - pow(l31,2) - pow(l32,2))
    L = np.array([[l11,0,0],[l21,l22,0],[l31,l32,l33]])
    LT = np.transpose(L)
    y = np.matmul(np.linalg.inv(L), B) 
    x = np.matmul(np.linalg.inv(LT), y)
    return x


def main():
    A = np.array([[4, 0, 2],[0, 4, 1],[2, 1, 2]])
    B = np.array([[1.5],[4.0],[2.5]])
    re = Cholesky(A,B)
    print(re)
    pass


if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
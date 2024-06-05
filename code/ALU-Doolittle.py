import numpy as np
from math import *

def Cholesky(A,B):
    a = A[0][0]
    b = A[0][1]
    c = A[0][2]
    d = A[1][0] / a
    e = A[1][1] - d*b
    f = A[1][2] - d*c
    g = A[2][0] / a
    h = (A[2][1] - g*b)/e
    i = A[2][2] - g*c - h*f

    L = np.array([[1,0,0],[d,1,0],[g,h,1]])
    U = np.array([[a,b,c],[0,e,f],[0,0,i]])
    y = np.matmul(np.linalg.inv(L), B) 
    x = np.matmul(np.linalg.inv(U), y)
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
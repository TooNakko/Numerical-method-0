import numpy as np
from math import *

def Jacobi4(A,B, x0, err = 10e-5): #FOR 4x4
    def f1(x2,x3,x4):
        return - x2*A[0][1] /A[0][0] - x3 * A[0][2]/A[0][0] - x4 * A[0][3]/A[0][0] + B[0]/A[0][0]
    def f2(x1,x3,x4):
        return - x1*A[1][0] /A[1][1] - x3 * A[1][2]/A[1][1] - x4 * A[1][3]/A[1][1] + B[1]/A[1][1]
    def f3(x1,x2,x4):
        return - x1*A[2][0] /A[2][2] - x2 * A[2][1]/A[2][2] - x4 * A[2][3]/A[2][2] + B[2]/A[2][2]
    def f4(x1,x2,x3):
        return - x1*A[3][0] /A[3][3] - x2 * A[3][1]/A[3][3] - x3 * A[3][2]/A[3][3] + B[3]/A[3][3]
    i  = 0
    xi = []
    xi.append(x0)
    while(i<40):
        xi.append([f1(xi[-1][1],xi[-1][2],xi[-1][3])[0], f2(xi[-1][0],xi[-1][2],xi[-1][3])[0], f3(xi[-1][0],xi[-1][1],xi[-1][3])[0], f4(xi[-1][0],xi[-1][1],xi[-1][2])[0]])
        i+=1 
        if(abs(xi[-1][0] + xi[-1][1] + xi[-1][2] + xi[-1][3] - (xi[-2][0] + xi[-2][1] + xi[-2][2] + xi[-2][3])) < err):
            break
    return xi

def Jacobi3(A,B, x0, err = 10e-5): #FOR 3x3
    def f1(x2,x3):
        return - x2*A[0][1] /A[0][0] - x3 * A[0][2]/A[0][0] + B[0]/A[0][0]
    def f2(x1,x3):
        return - x1*A[1][0] /A[1][1] - x3 * A[1][2]/A[1][1] + B[1]/A[1][1]
    def f3(x1,x2):
        return - x1*A[2][0] /A[2][2] - x2 * A[2][1]/A[2][2] + B[2]/A[2][2]

    i  = 0
    xi = []
    xi.append(x0)
    while(i<40):
        xi.append([f1(xi[-1][1],xi[-1][2])[0], f2(xi[-1][0],xi[-1][2])[0], f3(xi[-1][0],xi[-1][1])[0]])
        i+=1 
        if(abs(xi[-1][0] + xi[-1][1] + xi[-1][2] - (xi[-2][0] + xi[-2][1] + xi[-2][2] )) < err):
            break
    return xi
def GaussSidel4(A,B, x0, err = 10e-5): #FOR 4x4
    def f1(x2,x3,x4):
        return - x2*A[0][1] /A[0][0] - x3 * A[0][2]/A[0][0] - x4 * A[0][3]/A[0][0] + B[0]/A[0][0]
    def f2(x1,x3,x4):
        return - x1*A[1][0] /A[1][1] - x3 * A[1][2]/A[1][1] - x4 * A[1][3]/A[1][1] + B[1]/A[1][1]
    def f3(x1,x2,x4):
        return - x1*A[2][0] /A[2][2] - x2 * A[2][1]/A[2][2] - x4 * A[2][3]/A[2][2] + B[2]/A[2][2]
    def f4(x1,x2,x3):
        return - x1*A[3][0] /A[3][3] - x2 * A[3][1]/A[3][3] - x3 * A[3][2]/A[3][3] + B[3]/A[3][3]
    i  = 0
    xi = []
    xi.append(x0)
    while(i<40):
        x1 = f1(xi[-1][1],xi[-1][2],xi[-1][3])[0]
        x2 = f2(x1,xi[-1][2],xi[-1][3])[0]
        x3 = f3(x1,x2,xi[-1][3])[0]
        x4 = f4(x1,x2,x3)[0]
        xi.append([x1,x2,x3,x4])
        i+=1 
        if(abs(xi[-1][0] + xi[-1][1] + xi[-1][2] + xi[-1][3] - (xi[-2][0] + xi[-2][1] + xi[-2][2] + xi[-2][3])) < err):
            break
    return xi

def GaussSidel3(A,B, x0, err = 10e-5): #FOR 3x3
    def f1(x2,x3):
        return - x2*A[0][1] /A[0][0] - x3 * A[0][2]/A[0][0] + B[0]/A[0][0]
    def f2(x1,x3):
        return - x1*A[1][0] /A[1][1] - x3 * A[1][2]/A[1][1] + B[1]/A[1][1]
    def f3(x1,x2):
        return - x1*A[2][0] /A[2][2] - x2 * A[2][1]/A[2][2] + B[2]/A[2][2]

    i  = 0
    xi = []
    xi.append(x0)
    while(i<40):
        xi.append([f1(xi[-1][1],xi[-1][2])[0], f2(xi[-1][0],xi[-1][2])[0], f3(xi[-1][0],xi[-1][1])[0]])
        i+=1 
        if(abs(xi[-1][0] + xi[-1][1] + xi[-1][2] - (xi[-2][0] + xi[-2][1] + xi[-2][2] )) < err):
            break
    return xi



def main():
    A = np.array([[10, -1, 2,0],[-1, 11, -1, 3],[2, -1, 10, -1],[0,3,-1,8]])
    B = np.array([[6],[2.5],[-11],[15]])
    x0 = [0,0,0,0]
    re_gs = list(GaussSidel4(A,B, x0))
    re_jc = list(Jacobi4(A,B, x0))
    for r in re_gs:
        print("Gauss-sidel: x0 = {:.6f} | x1 = {:.6f} | x2 = {:.6f} | x3 = {:.6f}".format(r[0], r[1], r[2], r[3]))
    for r in re_jc:
        print("Jacobi: x0 = {:.6f} | x1 = {:.6f} | x2 = {:.6f} | x3 = {:.6f}".format(r[0], r[1], r[2], r[3]))


        
    print("========================\n\n\n")
    A = np.array([[4, 1, -1],[-1, 3, 1],[2, 2, 5]])
    B = np.array([[5],[-4],[1]])
    x0 = [0,0,0]
    re = list(Jacobi3(A,B, x0))
    for r in re:
        print("x0 = {:.6f} | x1 = {:.6f} | x2 = {:.6f}".format(r[0], r[1], r[2]))
    
    
    return

if __name__ == "__main__":
    main()
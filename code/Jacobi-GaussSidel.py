import numpy as np
from math import *

def CheckNormJac(A):
    I = np.identity(len(A))
    IA = I - A
    reF = 0
    for i in IA:
        for j in i:
            reF += j**2

    reF = sqrt(reF)

    reRow_arr = []
    reCol_arr = np.zeros_like(A[0])
    for i in range(len(IA)):
        reR = 0
        for j in range(len(A)):
            reR += abs(IA[i][j])
            reCol_arr[j] += abs(IA[i][j]) 
        reRow_arr.append(reR)

    reCol = max(reCol_arr)
    reRow = max(reRow_arr)

    if(reCol < 1 or reRow < 1 or reF < 1):
        return 1, reF, reCol, reRow
    return 0, reF, reCol, reRow

def CheckNormGauss(A):
    U = np.triu(A, k = 1)
    L = np.tril(A, k = -1)
    print(L)
    print("\n")
    print(U)
    I = np.identity(len(A))
    C = - np.matmul(np.linalg.inv(I + L),U)
    reF = 0
    for i in C:
        for j in i:
            reF += j**2

    reF = sqrt(reF)

    reRow_arr = []
    reCol_arr = np.zeros_like(A[0])
    for i in range(len(C)):
        reR = 0
        for j in range(len(A)):
            reR += abs(C[i][j])
            reCol_arr[j] += abs(C[i][j]) 
        reRow_arr.append(reR)

    reCol = max(reCol_arr)
    reRow = max(reRow_arr)

    if(reCol < 1 or reRow < 1 or reF < 1):
        return 1, reF, reCol, reRow
    return 0, reF, reCol, reRow





    pass


def Jacobi4(A,B, x0, err): #FOR 4x4
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

def Jacobi3(A,B, x0, err ): #FOR 3x3
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
def GaussSidel4(A,B, x0, err ): #FOR 4x4
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

def GaussSidel3(A,B, x0, err ): #FOR 3x3
    def f1(x2,x3):
        return - x2*A[0][1] / A[0][0] - x3 * A[0][2]/A[0][0] + B[0]/A[0][0]
    def f2(x1,x3):
        return - x1*A[1][0] / A[1][1] - x3 * A[1][2]/A[1][1] + B[1]/A[1][1]
    def f3(x1,x2):
        return - x1*A[2][0] / A[2][2] - x2 * A[2][1]/A[2][2] + B[2]/A[2][2]

    i  = 0
    xi = []
    xi.append(x0)
    while(i<40):
        xi.append([f1(xi[-1][1],xi[-1][2])[0], f2(xi[-1][0],xi[-1][2])[0], f3(xi[-1][0],xi[-1][1])[0]])
        i+=1 
        if(abs(xi[-1][0] + xi[-1][1] + xi[-1][2] - (xi[-2][0] + xi[-2][1] + xi[-2][2] )) < err):
            break
    return xi

def Normalize(A):
    A = A.astype(float) 
    for i in range(len(A)):
        max_e = A[i][i]
        for j in range(len(A)):
            A[i][j] = float(A[i][j]) / max_e
    return A    


def main():
    err = 10e-4
    A = np.array([[6, 2, 0.8],  # tong cua cac thanh phan ngaoi duong cheo chinh phai nho hon no
                [3, 5, 1],
                [0, 1.1, 2]])
    B = np.array([[12.5],[18.5],[-11.5]])
    x0 = [0,0,0,0]
    A = Normalize(A)
    print(A)
    checkJac, FJac, ColJac, RowJac = CheckNormJac(A)
    checkGauss, FGauss, ColGauss, RowGauss = CheckNormGauss(A)
    print("Jacobian:     Frobenius norm = {:.6f}, Column Norm = {:.6f}, Row Norm = {:.6f}\n".format(FJac, ColJac, RowJac))
    print("Gauss-Siedel: Frobenius norm = {:.6f}, Column Norm = {:.6f}, Row Norm = {:.6f}\n".format(FGauss, ColGauss, RowGauss))
    if checkJac == 0:
        print("Không thể áp dụng phương pháp Jacobian. Cả ba chuẩn Frobenius, chuẩn Cột và chuẩn hàng đều >=1")
    else:
        re_jc = list(Jacobi3(A,B, x0, err))
        for r in re_jc:
            print("Jacobi: x0 = {:.6f} | x1 = {:.6f} | x2 = {:.6f}".format(r[0], r[1], r[2]))


    if checkGauss == 0:
        print("Không thể áp dụng phương pháp Gauss-Siedel. Cả ba chuẩn Frobenius, chuẩn Cột và chuẩn hàng đều >=1")
    else:
        re_gs = list(GaussSidel3(A,B, x0, err))
        for r in re_gs:
            print("Gauss-sidel: x0 = {:.6f} | x1 = {:.6f} | x2 = {:.6f}".format(r[0], r[1], r[2]))





if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
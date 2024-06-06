import numpy as np
from math import *




def PowerMethod2(A,x0, err = 10e-4):
    x_arr = []
    lamd_arr = []
    x_arr.append(x0)
    idx = 0
    while idx < 40:
        x_new = np.matmul(A, x_arr[-1])
        lamd_arr.append(max(x_new))
        max_x = max(x_new)
        x_new = np.divide(x_new, max_x)
        x_arr.append(x_new)
        
        print("EIGEN = {}, VECTOR = ".format(lamd_arr[-1]))
        print(x_arr[-1])
        idx+=1
        if(len(x_arr) >=3):
            if abs(lamd_arr[idx-1] - lamd_arr[idx-2]) < err:
                break
    return lamd_arr, x_arr


def InversedMethod(A,x0, err = 10e-4):
    x_arr = []
    lamd_arr = []
    x_arr.append(x0)
    idx = 0
    while idx < 40:
        x_new = np.matmul(np.linalg.inv(A), x_arr[-1])
        lamd_arr.append(max(x_new))

        max_x = max(x_new)  
        x_new = np.divide(x_new, max_x)
        x_arr.append(x_new)

        idx+=1

        if(len(x_arr) >3 and (abs(x_arr[-1] - x_arr[-3]) < err).all() ):

                break
    final_eigen_vec = np.matmul(A, x_arr[-1])
    final_eigen_val = min(final_eigen_vec)
    return lamd_arr, x_arr, final_eigen_val

def main():
    A = np.array([[0, 1],[1, 1]]).astype(np.float32)
    x0 = np.array([[1],[1]]).astype(np.float32)

    #re = PowerMethod(A,x0)
    re, eigen_mat = PowerMethod2(A,x0)
    re_, eigen_mat_, final_eigen_val = InversedMethod(A,x0)
    print(len(re))
    print(len(eigen_mat))
    for r in range(len(re)):
        print(" x{} = {:.6f}, eigen vector: {}".format(r, re[r][0], np.transpose(eigen_mat[r+1])))
    print("+++++++++++++++++++++\n")

    for r in range(len(re_)):
        print(" x{} = {:.6f}, eigen vector = {}".format(r, re_[r][0], np.transpose(eigen_mat_[r+1])))
    print("Final eigen value = ", final_eigen_val[0])
    pass


if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
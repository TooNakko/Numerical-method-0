import numpy as np
from math import *

def PowerMethod(A,x0, err = 10e-4):
    x_arr = []
    lamd_arr = []
    x_arr.append(x0)
    idx = 0
    while idx < 40:
        x_new = np.matmul(A, x_arr[-1])

        lamd_arr.append(max(x_new) / max(x_arr[-1]))
        x_arr.append(x_new)

        idx+=1
        if(len(x_arr) >=3):
            if abs(lamd_arr[idx-1] - lamd_arr[idx-2]) < err:
                break
    return lamd_arr


def main():
    A = np.array([[-2, -3],[6, 7]])
    x0 = np.array([[1],[1]])
    re = PowerMethod(A,x0)
    for r in range(len(re)):
        print(" x{} = {:.6f}".format(r, re[r][0]))

    pass


if __name__ == "__main__":
    main()
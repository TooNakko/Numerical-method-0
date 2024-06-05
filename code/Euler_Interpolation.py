import numpy as np
from math import *



def f(y,t):
    return 1/pow(t,2) - y/t - pow(y,2) 

def Euler(t0, t_upper, y0, h):
    t_arr = []
    y_arr = []
    t_arr.append(t0)
    y_arr.append(y0)
    idx = 0
    while True:
        ynew = y_arr[-1] + h * f(y_arr[-1], t_arr[-1])
        tnew = t_arr[-1] + h
        y_arr.append(ynew)
        t_arr.append(tnew)
        if tnew >= t_upper:
            break 
    return y_arr, t_arr


def main():
    h = 0.05
    y0 = -1
    t0 = 1
    t_upper = 2
    
    y_arr, t_arr = Euler(t0,t_upper, y0, h)
    for i in range(len(y_arr)):
        print("t = {:.6f} | y = {:.6f}".format(t_arr[i], y_arr[i]))
    pass



if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
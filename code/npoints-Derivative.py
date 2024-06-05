import numpy as np
from numpy import *
import math
def f(x):
    return pow(math.e, 2*x)

def d_f(x):
    h = 1e-6
    return (f(x+h)-f(x-h))/(2*h)

def npointD(method, x, h, fx_arr, maxd):
    x = float(x)
    re = 0
    if method == "3end":
        try:
            #re = 1/2*h + [-3 * f(x) + 4*f(x+h) - f(x+2*h)]
            re = 1/(2*h) * (-3 * fx_arr[round(x,maxd)] + 4*fx_arr[round(x+h,maxd)] - fx_arr[round(x+2*h,maxd)])

        except Exception:
            print("Index error found, please choose another method")
            return 0
    elif method == "3mid":
        try:
            #re = 1/2*h * [f(x + h) - f(x-h)]
            re = 1/(2*h) * (fx_arr[round(x+h,maxd)] - fx_arr[round(x-h,maxd)])
        except Exception:
            print("Index error found, please choose another method")
            return 0
    elif method == "5end":
        try:
            #re = 1 / (12 * h) * [-25*f(x) + 48 * f(x+h) - 36 * f(x+2*h) + 16 * f(x+3*h) - 3*f(x + 4*h)]
            re = 1 / (12 * h) * (-25*fx_arr[round(x,maxd)] + 48 * fx_arr[round(x+h,maxd)] - 36 * fx_arr[round(x+2*h,maxd)] + 16 * fx_arr[round(x+3*h,maxd)] - 3*fx_arr[round(x+4*h,maxd)])

        except Exception:
            print("Index error found, please choose another method")
            return 0    
    elif method == "5mid":
        try:
            #re = 1 / (12 * h) * [f(x - 2*h) -   8 * f(x-h)      + 8 * f(x+h)      - f(x + 2*h)]
            re = 1 / (12 * h) * (fx_arr[round(x-2*h,maxd)] - 8 * fx_arr[round(x-h,maxd)] + 8 * fx_arr[round(x+h,maxd)] - fx_arr[round(x+2*h,maxd)])
        except Exception:
            print("Index error found, please choose another method")
            return 0  
    else:
        print("Method is not valid, try again.")
        return 0
    return re


def main():
    fx_arr = {1.1: 9.025013, 1.2: 11.02318, 1.3:13.46374, 1.4: 16.44465}
    max_digits = 2
    h = -0.1
    method = "3end"
    x = 1.4
    re = npointD(method, x, h, fx_arr, max_digits)
    re_ = d_f(x)
    if re != 0:
        print("Result using {} method is {:.6f}. Result by directly calculating is {:.6f}".format(method, re, re_))
        print("Actual error = {:.6f}".format(re_ - re))
    pass

if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
import math
from numpy import *
def f(y,t):
    return 1/t**2 - y/t +- y**2
    pass

def df( y,t):
  eps = 10e-6
  return (f(t+eps, y) - f(t, y)) / eps
#
#def df(y,t):
#    return y - t**2 + 1 - 2 * t

def TaylorNOrder(n,h,t0,y0):
    if(n!=2):
        print("Please pick n = 2.")
        return 0,0
    T = 0
    idx = 1
    y_arr = []
    t_arr = []
    y_arr.append(y0)
    t_arr.append(t0)
    while idx<80:
        T = f(y_arr[-1], t_arr[-1]) + h**(n-1)/ math.factorial(n) * df(y_arr[-1], t_arr[-1])
        y = y_arr[-1] + h * T
        y_arr.append(y)
        t = t0 + h * idx
        t_arr.append(t)
        idx+=1
    
    
    return y_arr, t_arr



def main():
    n = 2
    y0 = -1
    t0 = 1
    h = 0.05


    re_y, re_t = TaylorNOrder(n,h,t0,y0)
    for i in range(len(re_y)):
        print("y({:.2f}) = {:.6f}".format(re_t[i], re_y[i]))
    pass

if __name__ == "__main__":
    main()
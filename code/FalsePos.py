import numpy as np
from numpy import cos, e, pi
import math
def f(x):
    return pow(e,x) + pow(2,-x) + 2 * cos(x * pi / 180) - 6

def calcp(p0,p1):
    return p1 - (f(p1) * (p1 - p0))/(f(p1) - f(p0))


def Falsepos(nrange, er):
    p_arrs = []
    p_arrs.append(nrange[0])
    p_arrs.append(nrange[1])
    print("p0 = {}\np1 = {}".format(p_arrs[0], p_arrs[-1]))
    p2 = calcp(p_arrs[0],p_arrs[1])
    print("p2 = ", p2)
    p_arrs.append(p2)
    cur_idx = 2
    while True:
        ff = f(p_arrs[cur_idx]) * f(p_arrs[cur_idx-1])
        if (ff > 0):
            p_new = calcp(p_arrs[cur_idx-2], p_arrs[cur_idx])
        else:
            p_new = calcp(p_arrs[cur_idx-1], p_arrs[cur_idx])
        p_arrs.append(p_new)
        f_new = f(p_new)
        print(
            '''
p_{0} = {1}
ff_{0} = {2}'''.format(cur_idx + 1, p_new ,f_new))
        cur_idx +=1
        if abs(f_new) < er or cur_idx > 20:
            break
    return p_arrs[len(p_arrs) - 1], f_new


def main():
    nrange = [1,2]
    re, f_err = Falsepos(nrange, 10e-8)
    print("\nFinal result: x = {}\nWith error = {}".format(re, f_err))
if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
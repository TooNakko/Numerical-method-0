from sympy import *
from numpy import cos, pi
from decimal import *


def f(x):
    return x**2 - 10 *cos(x)

def d_f(x):
    h = 1e-6
    return (f(x+h)-f(x-h))/(2*h)


def Newton(p0, err, final_sol):
    p_arrs = [p0]
    idx = 0
    while True:
        idx +=1
        p_arrs.append(p_arrs[ -1] - f(p_arrs[- 1]) / d_f(p_arrs[- 1]))
        try:
            if abs(abs(p_arrs[len(p_arrs) - 1]) - final_sol) < err or idx == 20:
                
                return p_arrs 
        except:
            continue
    

def main():
    p0 = -100
    getcontext().prec = 6

    final_sol = 1.3793646
    p_arrs = Newton(p0, 10e-5, final_sol)
    i = 0
    for p in p_arrs:
        print("Iteration {}: p = {}".format(i, p))
        i+=1
    print("\nFinal solution = ", p_arrs[-1])
    print("With error = ", abs(p_arrs[-1]) - final_sol)


if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 




















































    # V Y L R N
from sympy import *
from numpy import cos, pi
from decimal import *


def f(x):
    return cos(x) - x



def Newton(p0, p1,err, final_sol):
    p_arrs = [p0, p1]
    idx = 0
    while True:
        idx +=1
        p_arrs.append( p_arrs[-1] - ( f(p_arrs[-1]) * (p_arrs[-1]- p_arrs[-2]) ) / ( f(p_arrs[-1]) - f(p_arrs[-2]) + 10e-10 ) )
        try:
            if abs(abs(p_arrs[len(p_arrs) - 1]) - final_sol) < err or idx == 20 or abs(p_arrs[-1] - p_arrs[-2]) < err:    
                return p_arrs 
        except:
            continue
    

def main():
    p0 = 0.25
    p1 = pi/4
    getcontext().prec = 6

    final_sol = 1.3793646
    p_arrs = Newton(p0,p1, 10e-5, final_sol)
    i = 0
    for p in p_arrs:
        print("Iteration {}: p = {}".format(i, p))
        i+=1
    print("\nFinal solution = ", p_arrs[-1])
    print("With error = ", abs(p_arrs[-1]) - final_sol)


if __name__ == "__main__":
    main()



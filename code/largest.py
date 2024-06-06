from math import *
import random
def f(x):
    return sqrt(x-x**2)

def g(x,t0,t1,t2):
    return f(x) -La(x,t0,t1,t2) + 0.25  
def La(x, t0, t1, t2):
    final = 0
    Lf0 = ((x - t1)*(x - t2))/(((t0 - t1)*(t0 - t2)) +1e-12) * f(t0)
    Lf1 = ((x - t0)*(x - t2))/(((t1 - t0)*(t1 - t2)) +1e-12) * f(t1)
    Lf2 = ((x - t0)*(x - t1))/(((t2 - t0)*(t2 - t1)) +1e-12) * f(t2)
    final = Lf0 + Lf1 + Lf2
    
    return final


def main():
    t0 = 0
    t2 = 1
    n = 0
    x = 0.25
    max_val = -10e9
    err_pre = 10e10
    while (n<10e5):
        t1 = random.randint(0,1000000)/1000000
        g_ = g(x,t0,t1,t2)
        if t1 > max_val and abs(g_) < 10e-5 and abs(g_) < err_pre:
            print("Found {:.6f}, with error {:.6f}".format(t1, abs(g_)))
            max_val = t1
            err_pre = abs(g_)
        n+=1
    print("Max t1: {:.6f}".format(max_val))
    return




if __name__ == "__main__":
    main()
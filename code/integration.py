from math import *
import numpy as np

def f(x):
    return cos(x)**2

def Simpson(a,b,n):
    h = (b - a)/n
    h_ = 0
    final = 0
    for i in range(n+1):
        if(i == 0 or i == n):
            coef = 1
        else:
            if(i%2 == 1):
                coef = 4
            else:
                coef = 2
        final += h/3 * coef * f(a + h_)
        print("With x = {} | coef = {} | f = {:.6f} | final = {:.6f}".format(a+h_,coef,f(a + h_), final), end = "\n\n")

        h_ += h
    return final



def Trapezoidal(a,b,n):
    h = (b - a)/n
    h_ = 0
    final = 0
    for i in range(n+1):
        if(i == 0 or i == n):
            coef = 1
        else:
            coef = 2
        final += h/2 * coef * f(a + h_)
        print("With x = {} | f = {:.6f} | final = {:.6f}".format(a+h_,f(a + h_), final), end = "\n\n")

        h_ += h
    return final

def MidPoint(a,b,n):
    h = (b - a)/n
    temp_h = h
    temp_h_ = a
    final = 0
    mid = []
    for i in range(n):
        mid.append((temp_h_ + temp_h)/ 2)
        temp_h_ += h
        temp_h += h
    for i in range(n):
        final += h * f(mid[i])
        print("With x_mid = {:.6f} | f = {:.6f}".format(mid[i], f(mid[i])), end = "\n\n")
        
    return final



def main():
    a = -0.5
    b = 0.5
    n = 10
    f = MidPoint(a,b,n)
    print("FINAL: {:.6f}".format(f))
    pass



if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
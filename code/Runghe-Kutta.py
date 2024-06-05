from math import *

def f(y,t):
    return (1+t)/(1+y)

def f_real(t):
    return sqrt(t**2 + 2*t + 6) - 1

def RungheKutta2(y0,t0,h, upper):
    y_arr = [y0]
    t_arr = [t0]
    idx = 1
    while t_arr[-1] < upper:
        k1 = f(y_arr[-1],t_arr[-1])
        k2 = f(y_arr[-1] + k1 * h, t_arr[-1] + h)
        y_arr.append(y_arr[-1] + h/2 * (k1 + k2))
        t_arr.append(t0 + h * idx)
        idx +=1
    
    return y_arr,t_arr

def main():
    t0 = 1
    y0 = 2
    h = 0.5
    upper = 2
    y_arr, t_arr = RungheKutta2(y0,t0,h, upper)
    for i in range(1,len(y_arr)):
        print("At t = {0}, y_({0}) = {1:.6f}, real value = {2:.6f} ".format(t_arr[i], y_arr[i], f_real(t_arr[i])))
    
    return



if __name__ == "__main__":
    main()
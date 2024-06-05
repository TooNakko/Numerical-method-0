from math import *
import numpy as np
def f(y,t):
    return (1+t)/(1+y)

def f_real(t):
    return sqrt(t**2 + 2*t + 6) - 1


def f_sys(t, Y):  # Y = [Y[0], Y[1]] where Y[0] = y1 and Y[1] = y2 in
  d_y1 = 3*Y[0] + 2*Y[1] - (2*t**2 + 1)*exp(2*t)
  d_y2 = 4*Y[0] + Y[1] + (t**2 + 2*t - 4)*exp(2*t)

  return np.array([d_y1, d_y2])

def RungheKutta2(y0,t0,h, upper):
    y_arr = [y0]
    t_arr = [t0]
    idx = 1
    while t_arr[-1] < upper:
        k1 = f_sys(y_arr[-1],t_arr[-1])
        k2 = f_sys(y_arr[-1] + k1 * h, t_arr[-1] + h)
        y_arr.append(y_arr[-1] + h/2 * (k1 + k2))
        t_arr.append(t0 + h * idx)
        idx +=1
    
    return y_arr,t_arr

def RungheKutta4(y0,t0,h, upper):
    y_arr = [y0]
    t_arr = [t0]
    idx = 1
    while t_arr[-1] < upper:
        k1 = f(y_arr[-1],t_arr[-1])
        k2 = f(y_arr[-1] + k1 * h/2, t_arr[-1] + h/2)
        k3 = f(y_arr[-1] + k2 * h/2, t_arr[-1] + h/2)
        k4 = f(y_arr[-1] + k3 * h, t_arr[-1] + h)
        
        y_arr.append(y_arr[-1] + h/6 * (k1 + 2*k2 + 2*k3 + k4))
        t_arr.append(t0 + h * idx)
        idx +=1
    
    return y_arr,t_arr

def RungheKutta4Sys(Y,t,h, upper):
    for i in range(len(t) - 1):
        k1 = f_sys(t[i]      , Y[i]         )
        k2 = f_sys(t[i] + h/2, Y[i] + k1*h/2)
        k3 = f_sys(t[i] + h/2, Y[i] + k2*h/2)
        k4 = f_sys(t[i] + h  , Y[i] + k3*h  )
        Y_next = Y[i] + h*(k1 + 2*k2 + 2*k3 + k4)/6
        Y = np.vstack((Y, Y_next))
    return Y



def main():
    if 0: # One equation
        t0 = 1
        y0 = 2
        h = 0.5
        upper = 2
        y_arr, t_arr = RungheKutta2(y0,t0,h, upper)
        for i in range(1,len(y_arr)):
            fr = f_real(t_arr[i])
            print("At t = {0}, y_({0}) = {1:.6f}, real value = {2:.6f} -> error = {3:.6f}".format(t_arr[i], y_arr[i],fr ,abs(fr - y_arr[i])))
    
    if 1: #System of equations
        h = 0.2
        t0 = 0  # t0 = t[0] = 1
        upper = 1  # t_end
        t = np.linspace(t0, upper, int((upper - t0) + 1 / h))
        Y = np.array([[1, 1]]) # y1[t0] = 1, y2[t0] = 1
        y_arr = RungheKutta4Sys(Y,t,h, upper)
        for i in range(len(t)):
            print("At t = {:.2f}, y1 = {:.6f} and y2 = {:.6f}".format(t[i], y_arr[i][0], y_arr[i][1]))
    


    return



if __name__ == "__main__":
    main()
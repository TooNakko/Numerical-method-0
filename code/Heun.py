from math import *

def f(y,t):
    return t * pow(e, 3*t) - 2*y 

def f_real(t):
    return 1/5 * t * e**(3*t) - 1/25 * e**(3*t) + 1/25 * e**(-2*t) 

def Heun(t0,y0,h, upper):
    y_predict = [0]
    y_correct = [y0]
    t_arr = [t0]
    idx = 1
    while t_arr[-1] < upper:
        y_p = y_correct[-1] + h * f(y_correct[-1], t_arr[-1])
        y_predict.append(y_p)
        t_arr.append(t0 + idx * h)
        y_c = y_correct[-1] + h/2 * (f(y_correct[-1], t_arr[-1 - 1]) + h * f(y_predict[-1], t_arr[-1]))
        y_correct.append(y_c)
        idx +=1
    
    return y_correct, y_predict, t_arr

def main():
    t0 = 0
    y0 = 0
    h = 0.5
    upper = 1
    y_correct, y_predict, t_arr = Heun(y0,t0,h, upper)
    for i in range(1,len(y_correct)):
        fr = f_real(t_arr[i])
        print("At t = {}, y_predicted = {:.6f} and y_corrected = {:.6f}, real value = {:.6f} -> error = {:.6f}".format(t_arr[i], y_predict[i], y_correct[i], fr, abs(fr - y_correct[i])))
    
    return



if __name__ == "__main__":
    main()
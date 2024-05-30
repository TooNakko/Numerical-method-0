import numpy as np
from numpy import cos


def kko(x, f, f_coef):
    final = 0
    for i in range(len(f)):
        print("======== ", i)
        Lf = 1
        for j in range(len(f_coef)):
            if j == i:
                continue
            Lf *= (x - f_coef[j])/(f_coef[i] - f_coef[j])
            print(Lf)
        Lf *= f[i]
        print(Lf)
        final += Lf
        #Lf_arr.append()

    return final


f_coef = [8.1, 8.3, 8.6, 8.7]
f = [16.94410, 17.56492, 18.50515, 18.82091]
Lf_arr = []

out = kko(8.4, f, f_coef)
print(out)


    
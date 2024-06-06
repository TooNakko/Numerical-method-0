import numpy as np
from numpy import cos


def kko(x, f, f_coef):
    final = 0
    for i in range(len(f)):
        Lf = 1
        for j in range(len(f_coef)):
            if j == i:
                continue
            Lf *= (x - f_coef[j])/(f_coef[i] - f_coef[j])
        Lf *= f[i]
        final += Lf
        #Lf_arr.append()

    return final

f_coef = [1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2]
f = [-1.00, -0.95, -0.904535, -0.863007, -0.824917, -0.789848, -0.757447 , -0.727415, -0.699495, -0.673467, -0.649141, -0.626350, -0.604949, -0.584812, -0.565825 , -0.547890, -0.530918 , -0.514832, -0.499561, -0.485043, -0.471220]

Lf_arr = []

out = kko(1.978, f, f_coef)
print(out)

print("\n======================")    
print(" Ngạc Anh Kiệt - 21020690")
print("======================\n") 
    
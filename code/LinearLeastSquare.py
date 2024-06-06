import numpy as np
import matplotlib.pyplot as plt

def LinearLeastSquare(y_arr,x_arr):
    xx_arr = []
    yx_arr = []
    for i in range(len(x_arr)):
        xx_arr.append(x_arr[i]**2)
        yx_arr.append(x_arr[i]*y_arr[i])

    a0 = (np.sum(xx_arr) * np.sum(y_arr) - np.sum(yx_arr) * np.sum(x_arr))/(len(x_arr) * np.sum(xx_arr) - np.sum(x_arr)**2)
    a1 = (len(x_arr) * np.sum(yx_arr) - np.sum(x_arr) * np.sum(y_arr))/(len(x_arr) * np.sum(xx_arr) - np.sum(x_arr)**2)
    return a1,a0





def main():
    y_arr = [1.0, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2]
    x_arr = [-1.00, -0.95, -0.904535, -0.863007, -0.824917, -0.789848, -0.757447 , -0.727415, -0.699495, -0.673467, -0.649141, -0.626350, -0.604949, -0.584812, -0.565825 , -0.547890, -0.530918 , -0.514832, -0.499561, -0.485043, -0.471220]
    a1,a0 = LinearLeastSquare(y_arr, x_arr)
    print("a1 = {:.6f}\na0 = {:.6f}".format(a1,a0))
    x = np.linspace(min(x_arr),max(x_arr),10)
    y = a1*x + a0
    plt.scatter(x_arr, y_arr)
    plt.plot(x, y)
    plt.show()
    pass




if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
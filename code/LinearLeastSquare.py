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
    y_arr = [2,4,6]
    x_arr = [1.764,0.975, 0.8571]
    a1,a0 = LinearLeastSquare(y_arr, x_arr)
    print("a1 = {:.6f}\na0 = {:.6f}".format(a1,a0))
    x = np.linspace(0,3,10)
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
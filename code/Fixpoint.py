
import random
def f(x):
    return x**2 - 4

def df(x):
    h = 1e-6
    return (f(x+h)-f(x-h))/(2*h)



def g(x):
    return x  - f(x)/df(x)

def FixPoint(x0, err = 10e-6):
    while 1:
        try: 
            a = f(x0)
            a = g(x0)
            break
        except:
            continue
    x_arr =  []
    x_arr.append(x0)
    idx = 0
    while 1:
        x_arr.append(g(x_arr[-1]))
        idx+=1
        if(abs(x_arr[-1] - x_arr[-2]) < err or idx > 40):
            break

    return x_arr



def main():
    x0 = random.randint(0,100)/10

    re = FixPoint(x0)
    for i in range(len(re)):
        print("x_{} = {:.6f}".format(i, re[i]))




if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
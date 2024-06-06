import math


def Maclaurin(x,n):
    final = 0
    for i in range(n + 1):
        final += 1 / (math.factorial(i)  + 10e-12) * pow(x,i)
    return final


def main():
    _1 = Maclaurin(-10, 90)
    _2 = 1 / Maclaurin(10, 90)
    print("Method 1: {}\nMethod 2: {}".format(_1, _2))
    




if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
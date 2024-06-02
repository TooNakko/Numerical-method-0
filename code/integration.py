def f(x):
    return 1 / x

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
        print("With x = {} | coef = {} | f = {} | final = {}".format(a+h_,coef,f(a + h_), final), end = "\n\n")

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
        print("With x = {} | f = {} | final = {}".format(a+h_,f(a + h_), final), end = "\n\n")

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
        print("With x = {} | f = {} | final = {}".format(mid[i], f(mid[i]), final), end = "\n\n")
        
    return final



def main():
    a = 1
    b = 2
    n = 2
    f = Simpson(a,b,n)
    print("FINAL: ",f)
    pass



if __name__ == "__main__":
    main()
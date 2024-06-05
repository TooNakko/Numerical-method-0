def f(x):
    return (x+2) * pow((x+1),2) * x * pow((x-1),3) * (x-2)



def Bisec(nranges, e):
    pre_p = 0
    idx  = 1
    ps = []
    idxs = []
    res = []
    for nrange in nranges:
        while True:
            p = (nrange[0] + nrange[1])/2        
            re = f(p)
            if re == 0 or  abs(p - pre_p) < e or idx == 100:
                ps.append(p)
                idxs.append(idx)
                res.append(re)
                break
            if re * f(nrange[0]) > 0: #If re's sign is the same with f(nrange[0])
                lower = p
                upper = nrange[1]
            else:
                lower = nrange[0]
                upper = p
            nrange = [lower, upper]

            print(
            '''
p_{0} = {1}
re_{0} = {2}
range_{0} = {3}
error_{0} = {4}
            '''.format(idx, p, re, nrange, abs(p - pre_p)))
            idx +=1
            pre_p = p
    return ps, idxs, res




def main():
    nranges = [[-0.5, 2.5], [-0.5, 2.4], [-0.5, 3], [-3, -0.5]]

    ps, idxs, res = Bisec(nranges, 10e-8)
    print('\n\n')
    for i in range(len(ps)):
        print("Range {0}: Loop {1} times, solution = {2} at f() = {3}\n".format(nranges[i], idxs[i], ps[i], res[i]))

if __name__ == "__main__":
    main()
    print("\n======================")    
    print(" Ngạc Anh Kiệt - 21020690")
    print("======================\n") 
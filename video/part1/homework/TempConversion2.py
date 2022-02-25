Temp = input()
if Temp[0] in ['C','c']:
    #print(Temp[1:-1])  --注意这里的-1在切片中不包括所以答案错误！
    F = eval(Temp[1:]) * 1.8 + 32
    #print(F)
    print("F{:.2f}".format(F))
elif Temp[0] in ['F','f']:
    C = (eval(Temp[1:])-32) / 1.8
    print("C%.2f" % C)

TempStr = input()
if TempStr[-1] in ['C','c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("%.s指摄氏度 %.2f 度" % (TempStr,F))
elif TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("%.s指华氏度%.2f度" % (TempStr,C))
else:
    print('输入格式错误')

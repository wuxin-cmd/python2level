# This is code to realize the conversion between Fahrenheit and Celsius temperatures

TempStr = input("Please input the value of temperature with symbol:")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1])-32)/1.8
    print("The temperature after conversion is {:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8 * eval(TempStr[0:-1]) + 32
    print("The temputerature afer conversion is {:.2f}F".format(F))
else:
    print("Input format error.")

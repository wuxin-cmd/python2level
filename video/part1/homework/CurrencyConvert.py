# This is a code to convert currency

#RMB 人民币
#USD 美元

money = input()

if money[0:3] in ['USD','usd']:
    rmbs = eval(money[3:])*6.78
    print("RMB{:.2f}".format(rmbs))
elif money[0:3] in ['RMB','rmb']:
    usds = eval(money[3:])/6.78
    print("USD{:.2f}".format(usds))

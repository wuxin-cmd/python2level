number = input()

lst  = ['零','一','二','三','四','五','六','七','八','九']

for i in range(len(number)):
     print(lst[eval(number[i])],end='')

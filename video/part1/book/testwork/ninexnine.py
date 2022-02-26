for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{} = {:2}".format(j,i,i*j),end=' ')
    print('')  #相当于输出一个回车

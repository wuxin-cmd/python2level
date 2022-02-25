def function(string):
    s = "";
    for n in range(len(string)):
        if (n + 1) % 2 != 0:
            s = s + string[n];
            if len(string) == (n + 1):
                print(s);
        else:
            s = s + string[n];
            print(s);
            s = "";
            
n = eval(input())
s = 'Hello World'
if n == 0:
    print(s)
elif n > 0:
    function(s)
else:
    for i in s:
        print(i)

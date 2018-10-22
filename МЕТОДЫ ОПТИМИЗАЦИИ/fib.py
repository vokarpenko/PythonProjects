def f(x):
    return 2*(x**2)+2*x+7/2


a = -3
b = 7
ep = 0.5
delta = 0.2
l = abs((b-a))/ep
fib = []
fib.append(1)
fib.append(1)
i = 2
while True:
        if (fib[i-1]+fib[i-2]) <= l:
            fib.append(fib[i-1]+fib[i-2])
            i += 1
        else:
            fib.append(fib[i - 1] + fib[i - 2])
            break
print(fib)
n = len(fib)-1
x1 = a+(b-a)*fib[n-2]/fib[n]
x2 = a+(b-a)*fib[n-1]/fib[n]
y1 = f(x1)
y2 = f(x2)
while n!=2:
    print('1')
    if y1>y2:
        a=x1
        x1=x2
        x2=b-(x1-a)
        y1=y2
        y2=f(x2)
    else:
        b=x2
        x2=x1
        x1=a+(b-x2)
        y2=y1
        y1=f(x1)
    n -= 1
if round(x1,4) == round(x2,4):
    xmin =(x1+x1+delta)/2
else:
    xmin = (x1+x2)/2
print(xmin)

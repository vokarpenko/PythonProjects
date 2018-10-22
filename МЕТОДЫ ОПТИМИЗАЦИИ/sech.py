def f(x):
    return 2*(x**2)+2*x+7/2


a = -3
b = 7
ep = 0.5
n = 0
while abs(b-a) >= ep :
    gold = (1 + 5 ** (1 / 2)) / 2
    x1 = b - (b - a) / gold
    x2 = a + (b - a) / gold
    y1 = f(x1)
    y2 = f(x2)
    if y1 >= y2:
        a = x1
    else:
        b = x2
    n += 1
    if n % 10 == 0:
        a = x1
        b = x2
xmin = (a+b)/2
print(xmin)
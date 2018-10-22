from scipy.misc import derivative
print('введите n')
n = int(input())
print('введите epsilon')
ep = float(input())
output = str('a0')+'*x^'+str(n)
for i in range(1, n, 1):
            output += '+a'+str(i)+'*x^'+str(n-i)
output += '+a'+str(n)
print(output)
arr = []
for i in range(n+1):
    print('введите коэффициент a'+str(i))
    arr.append(float(input()))
print('введите промежуток ab')
a = int(input())
b = int(input())


def f(x):
    f0 = 0
    j = 0
    for i in range(n+1):
        f0 += arr[i]*x**(n-j)
        j += 1
    return f0


#main
if f(b)*derivative(f, b, 1, 2) > 0:
    Xn = b
    Xn1 = Xn - (f(Xn) * ep) / (f(Xn) - f(Xn - ep))
    while not (abs(Xn1 - Xn) <= ep):
        Xn = Xn1
        Xn1 = Xn - (f(Xn) * ep) / (f(Xn)-f(Xn - ep))
else:
    Xn = a
    Xn1 = Xn-(f(Xn)*ep)/(f(Xn+ep)-f(Xn))
    while not(abs(Xn1-Xn) <= ep):
        Xn = Xn1
        Xn1 = Xn-(f(Xn)*ep)/(f(Xn+ep)-f(Xn))

print('Answer =',Xn1)





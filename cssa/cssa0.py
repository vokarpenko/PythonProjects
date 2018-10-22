#import numpy as np
import Gauss
m = int(input('Введите степень многочлена '))
n = 0
x = []
y = []

f = open('xy.txt')
for line in f:
    row = [float(i) for i in line.split()]
    x.append(row[0])
    y.append(row[1])
    n += 1
a = [0 for i in range(m+1)]
mat = []
for i in range(m+1):
    mat.append([])
    for j in range(m+2):
        mat[i].append(0)
b = []
for i in range(m+1):
    for j in range(m+1):
        for k in range(len(x)):
            mat[i][j] += x[k]**(2*m-i-j)
i = 0
for k0 in range(m+1):
    sum = 0
    for k1 in range(len(y)):
        sum += x[k1]**(m-k0)*y[k1]
    mat[k0][m+1] = sum
Gauss.Gauss(mat,a)
output = str(a[0])+'*x^'+str(m)
for i in range(1, m+1, 1):
        if a[i] > 0:
            output += '+'+str(a[i])+'*x^'+str(m-i)
        else:
            output += str(a[i]) + '*x^' + str(m - i)
print(output)




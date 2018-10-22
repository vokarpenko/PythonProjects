import win32com.client
import Gauss
Excel = win32com.client.Dispatch("Excel.Application")
wb = Excel.Workbooks.Open(u'C:\\PyCharm Community Edition 2017.2.3\Projects\cssa\list.xls')
xls = wb.ActiveSheet
m0 = int(xls.Cells(2, 4).value)
k0 = int(xls.Cells(2, 5).value)
x = []
y = []
i = 1
while True:
    temp = xls.Cells(i + 1, 1).value
    if temp is None:
        break
    x.append(temp)
    temp = xls.Cells(i + 1, 2).value
    y.append(temp)
    n = i
    i += 1

def smooth(m, k, num, x, y):
    a = [0 for i in range(m + 1)]
    mat = []
    for i in range(m+1):
        mat.append([])
        for j in range(m+2):
            mat[i].append(0)
    for i in range(m+1):
        for j in range(m+1):
            for k0 in range(int(num-k/2),int(num+k/2)+1,1):
                mat[i][j] += x[k0]**(2*m-i-j)
    for i in range(m+1):
        sum = 0
        for k1 in range(int(num-k/2),int(num+k/2)+1,1):
            sum += x[k1]**(m-i)*y[k1]
        mat[i][m+1] = sum
    Gauss.Gauss(mat,a)
    print(a)
    sum = 0
    j = 0
    for i in range(m,-1,-1):
        sum += a[j]*x[num]**i
        j += 1
    y0 = round(sum,2)
    return y0


y0=[]
for i in range(len(y)):
    if (i<k0/2):
        y0.append(y[i])
    if (i>=k0/2)and(i<=n-k0/2-1):
        y0.append(smooth(m0,k0,i,x,y))
    if (i>n-k0/2-1):
        y0.append(y[i])
i = 2
for temp in y0:

    i = i + 1
wb.Save()

#wb.Close()
#Excel.Quit()
'''
output = str(a[0])+'*x^'+str(m)
for i in range(1, m+1, 1):
        if a[i] > 0:
            output += '+'+str(a[i])+'*x^'+str(m-i)
        else:
            output += str(a[i]) + '*x^' + str(m - i)
print(output)
'''





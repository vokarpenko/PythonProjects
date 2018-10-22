import win32com.client
Excel = win32com.client.Dispatch("Excel.Application")
wb = Excel.Workbooks.Open(u'C:\\PyCharm Community Edition 2017.2.3\Projects\\lists\\xls\\amur.xls')
xls = wb.ActiveSheet
n = 2


while xls.Cells(n, 1).value != '[0]':
    n += 1
n -= 1
kolvoListov = int(n/17)
for i in range(3,kolvoListov+3,1):
    xls.Cells(1, i).value = 'Длина '+str(i-2)
k = 2
m = 3
for i in range(n):
    xls.Cells(k,m).value = float(xls.Cells(i+1,2).value)
    k += 1
    if (i+1)%17 == 0:
        k = 2
        m += 1
for i in range(3,kolvoListov+3,1):
    xls.Cells(19, i).value = 'Угол '+str(i-2)
k = 20
m = 3

for i in range(kolvoListov*4):
    xls.Cells(k,m).value = float(xls.Cells(i+1+n,2).value)
    k+=1
    if (i+1)%4==0:
        k=20
        m+=1
for i in range(1,500,):
    xls.Cells(i, 1).value = None
    xls.Cells(i, 2).value = None

wb.Save()
wb.Close()
Excel.Quit()
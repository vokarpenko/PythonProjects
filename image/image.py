f = open('pwd.txt')
a = {}
for line in f:
    string = ''
    m = False
    for i in line:
        if i == ';':
            m = True
            continue
        if m and i != '\n':
            string += i

    if string not in a:
        a.update({string: 1})
    else:
        a.update({string: a.get(string)+1})
#print(a)
n = 10
while n != 0:
    maxx = 0
    for x, y in a.items():
        if y > maxx:
            maxx = y
            maxName = x
    print(maxName,'=',maxx)
    a.pop(maxName)
    n -= 1

from tkinter import *
from tkinter import ttk
from math import floor

root = Tk()
root.title(u'Судоку')
root.geometry('710x450+300+200')
root.resizable(False, False)
#design
t11 = Text(root,height=1,width=2,font='Arial 30')
t11.grid(row=1,column=1)
t12 = Text(root,height=1,width=2,font='Arial 30',)
t12.grid(row=1,column=2)
t13 = Text(root,height=1,width=2,font='Arial 30',)
t13.grid(row=1,column=3)
t14 = Text(root,height=1,width=2,font='Arial 30',)
t14.grid(row=1,column=4)
t15 = Text(root,height=1,width=2,font='Arial 30',)
t15.grid(row=1,column=5)
t16 = Text(root,height=1,width=2,font='Arial 30',)
t16.grid(row=1,column=6)
t17 = Text(root,height=1,width=2,font='Arial 30',)
t17.grid(row=1,column=7)
t18 = Text(root,height=1,width=2,font='Arial 30',)
t18.grid(row=1,column=8)
t19 = Text(root,height=1,width=2,font='Arial 30',)
t19.grid(row=1,column=9)
t21 = Text(root,height=1,width=2,font='Arial 30',)
t21.grid(row=2,column=1)
t22 = Text(root,height=1,width=2,font='Arial 30',)
t22.grid(row=2,column=2)
t23 = Text(root,height=1,width=2,font='Arial 30',)
t23.grid(row=2,column=3)
t24 = Text(root,height=1,width=2,font='Arial 30',)
t24.grid(row=2,column=4)
t25 = Text(root,height=1,width=2,font='Arial 30',)
t25.grid(row=2,column=5)
t26 = Text(root,height=1,width=2,font='Arial 30',)
t26.grid(row=2,column=6)
t27 = Text(root,height=1,width=2,font='Arial 30',)
t27.grid(row=2,column=7)
t28 = Text(root,height=1,width=2,font='Arial 30',)
t28.grid(row=2,column=8)
t29 = Text(root,height=1,width=2,font='Arial 30',)
t29.grid(row=2,column=9)
t31 = Text(root,height=1,width=2,font='Arial 30',)
t31.grid(row=3,column=1)
t32 = Text(root,height=1,width=2,font='Arial 30',)
t32.grid(row=3,column=2)
t33 = Text(root,height=1,width=2,font='Arial 30',)
t33.grid(row=3,column=3)
t34 = Text(root,height=1,width=2,font='Arial 30',)
t34.grid(row=3,column=4)
t35 = Text(root,height=1,width=2,font='Arial 30',)
t35.grid(row=3,column=5)
t36 = Text(root,height=1,width=2,font='Arial 30',)
t36.grid(row=3,column=6)
t37 = Text(root,height=1,width=2,font='Arial 30',)
t37.grid(row=3,column=7)
t38 = Text(root,height=1,width=2,font='Arial 30',)
t38.grid(row=3,column=8)
t39 = Text(root,height=1,width=2,font='Arial 30',)
t39.grid(row=3,column=9)
t41 = Text(root,height=1,width=2,font='Arial 30',)
t41.grid(row=4,column=1)
t42 = Text(root,height=1,width=2,font='Arial 30',)
t42.grid(row=4,column=2)
t43 = Text(root,height=1,width=2,font='Arial 30',)
t43.grid(row=4,column=3)
t44 = Text(root,height=1,width=2,font='Arial 30',)
t44.grid(row=4,column=4)
t45 = Text(root,height=1,width=2,font='Arial 30',)
t45.grid(row=4,column=5)
t46 = Text(root,height=1,width=2,font='Arial 30',)
t46.grid(row=4,column=6)
t47 = Text(root,height=1,width=2,font='Arial 30',)
t47.grid(row=4,column=7)
t48 = Text(root,height=1,width=2,font='Arial 30',)
t48.grid(row=4,column=8)
t49 = Text(root,height=1,width=2,font='Arial 30',)
t49.grid(row=4,column=9)
t51 = Text(root,height=1,width=2,font='Arial 30',)
t51.grid(row=5,column=1)
t52 = Text(root,height=1,width=2,font='Arial 30',)
t52.grid(row=5,column=2)
t53 = Text(root,height=1,width=2,font='Arial 30',)
t53.grid(row=5,column=3)
t54 = Text(root,height=1,width=2,font='Arial 30',)
t54.grid(row=5,column=4)
t55 = Text(root,height=1,width=2,font='Arial 30',)
t55.grid(row=5,column=5)
t56 = Text(root,height=1,width=2,font='Arial 30',)
t56.grid(row=5,column=6)
t57 = Text(root,height=1,width=2,font='Arial 30',)
t57.grid(row=5,column=7)
t58 = Text(root,height=1,width=2,font='Arial 30',)
t58.grid(row=5,column=8)
t59 = Text(root,height=1,width=2,font='Arial 30',)
t59.grid(row=5,column=9)
t61 = Text(root,height=1,width=2,font='Arial 30',)
t61.grid(row=6,column=1)
t62 = Text(root,height=1,width=2,font='Arial 30',)
t62.grid(row=6,column=2)
t63 = Text(root,height=1,width=2,font='Arial 30',)
t63.grid(row=6,column=3)
t64 = Text(root,height=1,width=2,font='Arial 30',)
t64.grid(row=6,column=4)
t65 = Text(root,height=1,width=2,font='Arial 30',)
t65.grid(row=6,column=5)
t66 = Text(root,height=1,width=2,font='Arial 30',)
t66.grid(row=6,column=6)
t67 = Text(root,height=1,width=2,font='Arial 30',)
t67.grid(row=6,column=7)
t68 = Text(root,height=1,width=2,font='Arial 30',)
t68.grid(row=6,column=8)
t69 = Text(root,height=1,width=2,font='Arial 30',)
t69.grid(row=6,column=9)
t71 = Text(root,height=1,width=2,font='Arial 30',)
t71.grid(row=7,column=1)
t72 = Text(root,height=1,width=2,font='Arial 30',)
t72.grid(row=7,column=2)
t73 = Text(root,height=1,width=2,font='Arial 30',)
t73.grid(row=7,column=3)
t74 = Text(root,height=1,width=2,font='Arial 30',)
t74.grid(row=7,column=4)
t75 = Text(root,height=1,width=2,font='Arial 30',)
t75.grid(row=7,column=5)
t76 = Text(root,height=1,width=2,font='Arial 30',)
t76.grid(row=7,column=6)
t77 = Text(root,height=1,width=2,font='Arial 30',)
t77.grid(row=7,column=7)
t78 = Text(root,height=1,width=2,font='Arial 30',)
t78.grid(row=7,column=8)
t79 = Text(root,height=1,width=2,font='Arial 30',)
t79.grid(row=7,column=9)
t81 = Text(root,height=1,width=2,font='Arial 30',)
t81.grid(row=8,column=1)
t82 = Text(root,height=1,width=2,font='Arial 30',)
t82.grid(row=8,column=2)
t83 = Text(root,height=1,width=2,font='Arial 30',)
t83.grid(row=8,column=3)
t84 = Text(root,height=1,width=2,font='Arial 30',)
t84.grid(row=8,column=4)
t85 = Text(root,height=1,width=2,font='Arial 30',)
t85.grid(row=8,column=5)
t86 = Text(root,height=1,width=2,font='Arial 30',)
t86.grid(row=8,column=6)
t87 = Text(root,height=1,width=2,font='Arial 30',)
t87.grid(row=8,column=7)
t88 = Text(root,height=1,width=2,font='Arial 30',)
t88.grid(row=8,column=8)
t89 = Text(root,height=1,width=2,font='Arial 30',)
t89.grid(row=8,column=9)
t91 = Text(root,height=1,width=2,font='Arial 30',)
t91.grid(row=9,column=1)
t92 = Text(root,height=1,width=2,font='Arial 30',)
t92.grid(row=9,column=2)
t93 = Text(root,height=1,width=2,font='Arial 30',)
t93.grid(row=9,column=3)
t94 = Text(root,height=1,width=2,font='Arial 30',)
t94.grid(row=9,column=4)
t95 = Text(root,height=1,width=2,font='Arial 30',)
t95.grid(row=9,column=5)
t96 = Text(root,height=1,width=2,font='Arial 30',)
t96.grid(row=9,column=6)
t97 = Text(root,height=1,width=2,font='Arial 30',)
t97.grid(row=9,column=7)
t98 = Text(root,height=1,width=2,font='Arial 30',)
t98.grid(row=9,column=8)
t99 = Text(root,height=1,width=2,font='Arial 30',)
t99.grid(row=9,column=9)


def readFromWindow():
    t = []
    for i in range(1,10,1):
       tt = []
       t.append(tt)
       for j in range(1,10,1):
            t0=eval('t'+str(i)+str(j)+'.get('+'1.0'+',END)')
            if t0 == '\n':
                tt.append(0)
            else:
                tt.append(int(t0))
    return initSolved(t)


def initSolved(in_val):
    suggest = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    solved = [[0] * 9 for i in range(9)]
    for i in range(9):
        for j in range(9):
            if in_val[i][j] != 0:
                solved[i][j] = [in_val[i][j], 'in', []]
            else:
                solved[i][j] = [0, 'unknown', suggest]
    return solved


def clear():
    for i in range(1,10,1):
       for j in range(1,10,1):
            eval('t'+str(i)+str(j)+'.delete('+'1.0'+',END)')
    return


def fileRead():
    with open("input.txt") as file:
        array = [row.strip() for row in file]
        t = []
        for i in range(len(array)):
            tt = []
            t.append(tt)
            for char in array[i]:
                tt.append(int(char))
    clear()
    for i in range(1,10,1):
        for j in range(1,10,1):
            if t[i-1][j-1] != 0:
                string = str(t[i-1][j-1])
                eval('t'+str(i)+str(j)+'.insert('+'1.0'+','+string+')')
    return


def solve():
    sudoku = readFromWindow()
    changed = 0
    steps = 0
    while True:
        changed = updateSuggests(sudoku)#сужение множества значений

        steps += 1
        if steps > 81:
            break
        if changed == 0:
            break
    if (not isSolved(sudoku))and (not isFailed(sudoku)):
        backtracking(sudoku) #поиск с возвратом
    if isSolved(sudoku):
        updateScreen(sudoku)
    return


def helpSolve(sudoku):
    sudoku = initSolved(sudoku)
    changed = 0
    steps = 0
    while True:
        changed = updateSuggests(sudoku)#сужение множества значений
        steps += 1
        if steps > 81:
            break
        if changed == 0:
            break
    if (not isSolved(sudoku))and (not isFailed(sudoku)):
        backtracking(sudoku) #поиск с возвратом
    if isSolved(sudoku):
        updateScreen(sudoku)
    return


def updateScreen(t):
    tt=t
    for i in range(9):
        for j in range(9):
            if tt[i][j]!=0:
                tt[i][j]=tt[i][j][0]
            else:
                tt[i][j]=''
    t=tt
    clear()
    for i in range(1,10,1):
        for j in range(1,10,1):
            if t[i-1][j-1] != 0:
                string = str(t[i-1][j-1])
                eval('t'+str(i)+str(j)+'.insert('+'1.0'+','+string+')')


def updateSuggests(solved):
    changed = 0
    for i in range(9):
        for j in range(9):
            if solved[i][j][1]!= 'unknown':
                continue
            changed += solveSingle(i,j,solved)
            changed += solveHiddenSingle(i,j,solved)
    return changed


def solveSingle(i,j,solved):
    solved[i][j][2] = arrayDiff(solved[i][j][2], rowContent(i,solved))
    solved[i][j][2] = arrayDiff(solved[i][j][2], colContent(j,solved))
    solved[i][j][2] = arrayDiff(solved[i][j][2], sectContent(i, j,solved))
    if len(solved[i][j][2]) == 1:
        markSolved(i,j,solved,solved[i][j][2][0])#наше найденное значение
        return 1
    return 0


def solveHiddenSingle(i,j,solved):
    less_suggest = lessRowSuggest(i, j,solved)
    changed = 0
    if len(less_suggest) == 1:
        markSolved(i,j,solved,less_suggest[0])
        changed+=1
    less_suggest = lessColSuggest(i,j,solved)
    if len(less_suggest) == 1:
        markSolved(i,j,solved,less_suggest[0])
        changed+=1
    less_suggest = lessSectSuggest(i,j,solved)
    if len(less_suggest) == 1:
        markSolved(i,j,solved,less_suggest[0])
        changed+=1
    return changed

def markSolved(i,j,solved,solve):
    solved[i][j][0] = solve
    solved[i][j][1] = 'solved'
    return


def rowContent(i,solved):
    content = []
    for j in range(9):
        if solved[i][j][1] !='unknown':
            content.append(solved[i][j][0])
    return content


def colContent(j,solved):
    content = []
    for i in range(9):
        if solved[i][j][1] != 'unknown':
            content.append(solved[i][j][0])
    return content


def lessRowSuggest(i,j,solved):
    less_suggest = solved[i][j][2]
    for x in range(9):
        if (x == j) or (solved[i][j][1] != 'unknown'):
            continue
        less_suggest= arrayDiff(less_suggest,solved[i][x][2])
    return less_suggest


def lessColSuggest(i,j,solved):
    less_suggest = solved[i][j][2]
    for x in range(9):
        if (x == i) or (solved[i][j][1] != 'unknown'):
            continue
        less_suggest= arrayDiff(less_suggest,solved[x][j][2])
    return less_suggest


def lessSectSuggest(i,j,solved):
    less_suggest = solved[i][j][2]
    offset = (floor(i/3)*3,floor(j/3)*3)
    for x in range(3):
        for y in range(3):
            if ((offset[0]+x == i)and(offset[1]+y == j)) or (solved[x+offset[0]][y+offset[1]][1] != 'unknown'):
                continue
            less_suggest= arrayDiff(less_suggest,solved[offset[0]+x][offset[1]+y][2])
    return less_suggest


def sectContent(i,j,solved):
    content = []
    offset = (floor(i/3)*3,floor(j/3)*3)
    for x in range(3):
        for y in range(3):
            if solved[offset[0]+x][offset[1]+y][1] != 'unknown':
                content.append(solved[offset[0]+x][offset[1]+y][0])
    return content


def arrayDiff(ar1,ar2):
    arr_diff=[]
    for i in range(len(ar1)):
        is_found = False
        for j in range(len(ar2)):
            if ar1[i] == ar2[j]:
                is_found = True
                break
        if not is_found:
            arr_diff.append(ar1[i])
    return arr_diff




def isSolved(solved):
    is_solved = True
    for i in range(9):
        for j in range(9):
            if solved[i][j][1] == 'unknown':
                is_solved = False
                return is_solved
    return is_solved


def isFailed(solved):
    is_failed =False
    for i in range(9):
        for j in range(9):
            if (('unknown' == solved[i][j][1]) and ( len(solved[i][j][2])==0) ):
                is_failed = True
                return is_failed
    if is_failed:
        print("FAIL")
    return is_failed


def backtracking(solved):
    in_val = [[0] * 9 for i in range(9)]
    i_min = -1
    j_min = -1
    suggests_cnt = 0
    for i in range(9):
        for j in range(9):
            in_val[i][j] = solved[i][j][0]
            if (solved[i][j][1] == 'unknown' and (len(solved[i][j][2])<suggests_cnt or not suggests_cnt)):
                suggests_cnt = len(solved[i][j][2])
                i_min = i
                j_min = j
    for k in range(suggests_cnt):
        in_val[i_min][j_min] = solved[i_min][j_min][2][k]
        helpSolve(in_val)
        if isSolved(solved):
            out_val = solved
            for i in range(9):
                for j in range(9):
                    markSolved(i,j,solved,out_val[i][j][0])
    return


go =ttk.Button(root,width=12,command=solve,text='Решить')
go.grid(row=1,column=18)
clearBtn = ttk.Button(width=12,command=clear,text='Очистить')
clearBtn.grid(row=1,column=22)
readfile = ttk.Button(width=17, command=fileRead, text='Считать из файла')
readfile.grid(row=1,column=20)
root.mainloop()
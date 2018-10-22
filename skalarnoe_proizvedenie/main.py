import numpy as np
A0 = []
f = open('input.txt')
for line in f:
    row = [float(i) for i in line.split()]
    if len(row) !=0:
        A0.append(row)


def matrix_souz(mat):
    matNP = np.array(mat)
    matNP = matNP.transpose()
    temp0 = mat
    for i in range(len(mat)):
        for j in range(len(mat)):
            temp=matNP
            temp = np.delete(temp,i,0)
            temp = np.delete(temp,j,1)
            det = np.linalg.det(temp)
            temp0[i][j] = det * (-1)**(i+j)
    return temp0


dlina = len(A0)
A = np.array(A0)
n = 0
while n != dlina:
    vector = []
    temp = []
    k = 2
    while True:
        vectorX = []
        for i in range(len(A)):
            vectorX.append(np.random.random())
        AT = A.transpose()
        if np.linalg.norm(np.dot(np.linalg.matrix_power(A,k),vectorX))==0:
            lamba = 0
            E = np.eye(len(A0))
            S = matrix_souz(A0 - lamba * E)
            for i0 in range(len(S)):
                sob_vector = S[:, i0]


            print('LAMBDA', n, '=', lamba, '  VECTOR', n, '=', sob_vector)
            break
        alpha = 1/np.linalg.norm(np.dot(np.linalg.matrix_power(A,k),vectorX))
        betta = 1 / np.linalg.norm(np.dot(np.linalg.matrix_power(AT, k), vectorX))
        topLeft = alpha * np.dot(np.linalg.matrix_power(A,k),vectorX)
        bottomLeft = alpha * np.dot(np.linalg.matrix_power(A,k-1),vectorX)
        topRight = betta * np.dot(np.linalg.matrix_power(AT,k),vectorX)
        bottomRight = topRight
        temp.append(np.sum(topLeft * topRight) / np.sum(bottomLeft * bottomRight))
        if k>=3:
            if round(temp[k-3], 4) == round(temp[k-2], 4):
                lamba = round(temp[k - 2], 4)
                vector = topLeft
                E=np.eye(len(A0))
                S=matrix_souz(A0-lamba*E)
                for i0 in range(len(S)):
                    sob_vector = S[:,i0]
                    sum = 0
                    for j0 in range(len(sob_vector)):
                        sum+= sob_vector[j0]**2
                    if sum!=0:
                        break
                sob_vector=(1/sob_vector[len(sob_vector)-1])*sob_vector
                print('LAMBDA',n,'=',lamba,'  VECTOR',n,'=',sob_vector)
                break
        k += 1
    if lamba==0:
        break
    H = np.eye(len(A))
    H[0][0] = 1/vector[0]
    for i in range(1,len(H),1):
        H[i][0] = -1*vector[i]/vector[0]
    B = np.dot(np.dot(H,A),np.linalg.inv(H))
    A1 = [[0 for i in range(len(B)-1)] for j in range(len(B)-1)]
    for i in range (1,len(B),1):
        for j in range(1,len(B),1):
            A1[i-1][j-1]=B[i][j]
    A = A1
    A = np.array(A)
    n += 1

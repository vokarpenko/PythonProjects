

def floydMin():
    minMatrix = [[1000 for i in range(n)] for j in range(n)]
    for vertex in graph:
        minMatrix[vertex[0] - 1][vertex[1] - 1] = graph.get(vertex)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                minMatrix[i][j] = min(minMatrix[i][j], minMatrix[i][k] + minMatrix[k][j])
    for i in range(n):
        for j in range(n):
            if minMatrix[i][j]!=1000:
                print('Кратчайший путь между вершинами %x и %y: %w'.replace('%x', str(i + 1)).replace('%y', str(j + 1))
                    .replace('%w', str(minMatrix[i][j])))


def floydMax():
    maxMatrix = [[0 for i in range(n)] for j in range(n)]
    for vertex in graph:
        maxMatrix[vertex[0] - 1][vertex[1] - 1] = graph.get(vertex)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if maxMatrix[i][k] > 0 and maxMatrix[k][j] > 0:
                    maxMatrix[i][j] = max(maxMatrix[i][j], maxMatrix[i][k] + maxMatrix[k][j])
    for i in range(n):
        for j in range(n):
            if maxMatrix[i][j]!=0:
                print('Максимальный путь между вершинами %x и %y: %w'.replace('%x', str(i + 1)).replace('%y', str(j + 1))
                  .replace('%w', str(maxMatrix[i][j])))


n = 11
graph = {(1, 2): 9, (1, 3): 11, (1, 4): 1, (2, 3): 6, (2, 4): 11, (2, 5): 2, (2, 6): 10, (3, 6): 9,
         (3, 7): 10, (4, 5): 6, (5, 6): 6, (5, 9): 5, (5, 10): 8, (6, 7): 10, (6, 8): 9, (6, 9): 7,
         (7, 8): 7, (8, 9): 8, (8, 11): 3, (9, 10): 8, (9, 11): 11, (10, 11): 7}
#floydMin()
floydMax()

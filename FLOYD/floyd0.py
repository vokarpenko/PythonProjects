

def floydmin():
    minMatrix = [[1000 for i in range(n)] for j in range(n)]
    for vertex in graph:
        minMatrix[vertex[0] - 1][vertex[1] - 1] = graph.get(vertex)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                minMatrix[i][j] = min(minMatrix[i][j], minMatrix[i][k] + minMatrix[k][j])
    for i in range(n):
        for j in range(n):
            print('Кратчайший путь между вершинами %x и %y: %w'.replace('%x', str(i + 1)).replace('%y', str(j + 1))
                  .replace('%w', str(minMatrix[i][j]) if minMatrix[i][j] != 1000 else 'нет пути'))


def floydmax():
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
            print('Максимальный путь между вершинами %x и %y: %w'.replace('%x', str(i + 1)).replace('%y', str(j + 1))
                  .replace('%w', str(maxMatrix[i][j]) if maxMatrix[i][j] != 0 else 'нет пути'))


n = 11
graph = {(1, 2): 3, (1, 3): 5, (1, 4): 7, (2, 3): 2, (2, 4): 3, (2, 5): 8, (2, 6): 2, (3, 6): 8,
         (3, 7): 2, (4, 5): 10, (5, 6): 6, (5, 9): 6, (5, 10): 10, (6, 7): 5, (6, 8): 9, (6, 9): 5,
         (7, 8): 2, (8, 9): 5, (8, 11): 1, (9, 10): 2, (9, 11): 2, (10, 11): 3}
floydmin()
#floydmax()
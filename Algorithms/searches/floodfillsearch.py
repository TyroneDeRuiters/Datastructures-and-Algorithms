def find(data, x, y, n, m, visited, maize):
    if(x >= n or y >= m):
        return False
    if(x < 0 or y < 0):
        return False
    if(visited[x][y] == True):
        return False
    if(maize[x][y] == data):
        return True
    visited[x][y] = True
    if(find(data, x - 1, y - 1, n, m, visited, maize) == True):
        return True
    if(find(data, x - 1, y, n, m, visited, maize) == True):
        return True
    if(find(data, x - 1, y + 1, n, m, visited, maize) == True):
        return True
    if(find(data, x , y - 1, n, m, visited, maize) == True):
        return True
    if(find(data, x, y, n, m, visited, maize) == True):
        return True
    if(find(data, x, y + 1, n, m, visited, maize) == True):
        return True
    if(find(data, x + 1, y - 1, n, m, visited, maize) == True):
        return True
    if(find(data, x + 1, y, n, m, visited, maize) == True):
        return True
    if(find(data, x + 1, y + 1, n, m, visited, maize) == True):
        return True
    return False

arr = [[1,6,7,14], [4, 8, 2,99], [0, 12, 55,-1]]
print(find(55, 0, 0, len(arr), len(arr[0]), [[False for i in range(len(arr[0]))] for j in range(len(arr))], arr))

def search(N, M, matrix, visitedMatrix, i, j):
    # field is already visited, or is water
    if visitedMatrix[i][j] == 1 or matrix[i][j] == 0:
        return True

    visitedMatrix[i][j] = 1

    # if examined field is on the border - not a closed island
    if i == 0 or j == 0 or i == N-1 or j == M-1:
        return False

    up = search(N, M, matrix, visitedMatrix, i-1, j)
    down = search(N, M, matrix, visitedMatrix, i+1, j)
    left = search(N, M, matrix, visitedMatrix, i, j-1)
    right = search(N, M, matrix, visitedMatrix, i, j+1)

    # closed island only if all 4 sides return True
    return up and down and left and right


def findClosedIslands(N, M, matrix):
    # create a matrix of the same size as the input matrix to track where we already visited
    visitedMatrix = [[0 for i in range(M)] for j in range(N)]

    closedIslands = 0

    # island on the borders = not a closed island so we can skip the first/last row/col checks
    for i in range(1, N-1):
        for j in range(1, M-1):
            if matrix[i][j] == 1 and visitedMatrix[i][j] == 0:
                # new island
                if search(N, M, matrix, visitedMatrix, i, j):
                    closedIslands += 1

    return closedIslands


if __name__ == "__main__":
    # example one
    matrixN = 5
    matrixM = 8
    matrix = [[0, 0, 0, 0, 0, 0, 0, 1],
              [0, 1, 1, 1, 1, 0, 0, 1],
              [0, 1, 0, 1, 0, 0, 0, 1],
              [0, 1, 1, 1, 1, 0, 1, 0],
              [1, 0, 0, 0, 0, 1, 0, 1]]
    
    
    # example two

    # matrixN = 3
    # matrixM = 3
    # matrix = [[1,0,0], [0,1,0], [0,0,1]]
    res = findClosedIslands(matrixN, matrixM, matrix)
    print(res)
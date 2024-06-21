def invalidNumber(sudoku, row, col, num):

    # row
    for i in range(9):
        if sudoku[row][i] == num:
            return True
    # column
    for i in range(9):
        if sudoku[i][col] == num:
            return True
    # square
    squareX = row - row % 3
    squareY = col - col % 3
    for i in range(3):
        for j in range(3):
            if sudoku[squareX + i][squareY + j] == num:
                return True

    return False


def findEmptySpot(sudoku, spot):
    for row in range(9):
        for col in range(9):
            if sudoku[row][col] == 0:
                spot[0] = row
                spot[1] = col
                return True
    return False


def solveSudoku(sudoku, spot=[0, 0]):

    if not findEmptySpot(sudoku, spot):
        return True

    row = spot[0]
    col = spot[1]

    for num in range(1, 10):
        if invalidNumber(sudoku, row, col, num):
            continue
        sudoku[row][col] = num
        if solveSudoku(sudoku, spot):
            return True
        sudoku[row][col] = 0
    return False


sudoku = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]


def printSudoku(sudoku):
    for i in range(9):
        for j in range(9):
            print(f"{sudoku[i][j]}, ", end=" ")
        print()


def findSolutionSudoku(sudoku):
    printSudoku(sudoku)
    if solveSudoku(sudoku):
        print("Solution:")
        printSudoku(sudoku)
    else:
        print("No solution finded")


findSolutionSudoku(sudoku)

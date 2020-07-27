import argparse
import datetime
def MazePathFinder(row, column):
    # checking the destination cell is zero or not
    if maze[SIZE-1][SIZE-1] == 0:
        return False
    # if destination is reached, maze is solved
    # checking the destination is the last cell(maze[SIZE-1][SIZE-1])
    if (row == SIZE - 1) and (column == SIZE - 1):
        solution[row][column] = 1
        return True
    # checking if we can visit in this cell or not
    # the indices of the cell must be in (0,SIZE-1)
    # and solution[r][c] == 0 is making sure that the cell is not already visited
    # maze[r][c] == 0 is making sure that the cell is not blocked
    if row >= 0 and column >= 0 and row < SIZE and column < SIZE and solution[row][column] == 0 and maze[row][column] == 1:
        # if safe to visit then visit the cell
        solution[row][column] = 1
        # going down
        if MazePathFinder(row + 1, column):
            return True
        # going right
        if MazePathFinder(row, column + 1):
            return True
        # going up
        if MazePathFinder(row - 1, column):
            return True
        # going left
        if MazePathFinder(row, column - 1):
            return True
        # backtracking
        solution[row][column] = 0
        return False
    return False


def printFoundPath(sol):
    outputFile.write("*\n" + "The path found for given inut:\n\n")
    for i in sol:
        for j in i:
            outputFile.write(" " + str(j) + " ")
        outputFile.write('\n')
    now = datetime.datetime.now()
    outputFile.write("\nTime stamp of executed file: " +
                     now.strftime("%Y-%m-%d*%H:%M:%S\n" + "*\n\n"))


if __name__ == "__main__":
    maze = []  # matrix will be build here
    parser = argparse.ArgumentParser()
    parser.add_argument("ipFile", help="Input file")
    parser.add_argument("opFile", help="Output file")
    args = parser.parse_args()

    inputFile = open(args.ipFile, 'r')  # input file arguments here
    outputFile = open(args.opFile, 'a')  # output file arguments here

    for data in inputFile:  # extracting data of input file and appending to maze list
        [i.strip('\n\r') for i in data]
        maze.append([int(x) for x in data.split()])

    SIZE = len(maze)
    # creating same size of matrix form to collect the path
    solution = [[0] * SIZE for _ in range(SIZE)]
    # solution matrix as providing input for printFoundPath function
    # initially giving row and column value as 0
    if (MazePathFinder(0, 0)):
        printFoundPath(solution)
    else:
        outputFile.write("***\n-1\n")
        # wring the solution of input matrix in output file
        outputFile.write("Didnt found the path for the given matrix")
        now = datetime.datetime.now()
        # wring the date in output file
        outputFile.write("\n Time stamp of executed file: " +
                         now.strftime("%Y-%m-%d*%H:%M:%S") + "\n***\n\n\n")

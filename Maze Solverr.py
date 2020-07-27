SIZE = int(input("Enter number of size of the maze: "))
maze = []
print("Enter the %s x %s matrix: " % (SIZE, SIZE))
for i in range(SIZE):
    maze.append(list(map(int, input().rstrip().split())))
# list to store the solution matrix
solution = [[0]*SIZE for _ in range(SIZE)]
print("The solution of the maze: ")

# function to solve the maze
# using backtracking


def MazePath(row, column):
    # if destination is reached, maze is solved
    # destination is the last cell(maze[SIZE-1][SIZE-1])
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
        if MazePath(row + 1, column):
            return True
        # going right
        if MazePath(row, column + 1):
            return True
        # going up
        if MazePath(row - 1, column):
            return True
        # going left
        if MazePath(row, column - 1):
            return True
        # backtracking
        solution[row][column] = 0
        return False
    return 0


if(MazePath(0, 0)):
    for i in solution:
        print(i)
else:
    print("-1")

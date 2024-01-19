# Backtracking Algorithm: 
# 1. Go to the first empty cell
#`2. Try all numbers (1-9)
# 3. Find a number that works in that cell (check row, column, and square)
# 4. Go to the next empty cell and repeat
# 5. If the solution does not work for a cell => Backtrack

def printGrid(grid):
    print("-------------------------")
    for i in range(len(grid)): # for every row
        if i % 3 == 0 and i != 0: # put a seperator line for every 3 rows
            print("-------------------------")
        for j in range(len(grid[0])): 
            if j % 3 == 0 and j != 0: # put a seperator line for every 3 columns
                print("| ", end="")
            if j == 0: # add a border on the left side of the grid
                print("| ", end="")
            if j == 8: # add a border on the right side of the grid
                print(str(grid[i][j]) + " |")
            else:
                print(str(grid[i][j]) + " ", end="") # print the value
    print("-------------------------")

def findEmpty(grid):
# function to find an empty cell
    for i in range(len(grid)): 
        for j in range(len(grid[0])):
            if grid[i][j] == 0: # if the cell is empty 
                return [i, j] # return row, col
    return None

def isValid(grid, num, pos):
# function to check if a number is valid
    # checking the row of that cell
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i: # column is changing, row is constant
            return False

    # checking the column of that cell
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i: # row is changing, column is constant
            return False

    # checking the box of that cell
    boxX = pos[1] // 3
    boxY = pos[0] // 3
    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

def backtracking(grid):
# function for the backtracking algorithm
    empty = findEmpty(grid) # finding an empty cell first
    if not empty: return True # if a cell is not empty
    else: row, col = empty # if a cell is empty get the position

    for i in range(1,10): # sudoku numbers (1-9)
        if isValid(grid, i, (row, col)): # all the possible numbers for that cell
            grid[row][col] = i # enter valid number
            if backtracking(grid): return True
            grid[row][col] = 0
    return False

def main(): # main function
        print("Welcome To Sudoku Solver!")
        print("")
        print("Enter values for each position on the grid.")
        print("Enter \"0\" if a cell is empty.")
        print("")
        grid = [[], [], [], [], [], [], [], [], []]
        gridFilled = False # is grill filled out
        while not gridFilled: # run while grill is not filled out
            for i in range(len(grid)): 
                for j in range(len(grid)):
                    val = int(input("Row: " + str(i + 1) + ", Column: " + str(j + 1) + " = ")) # ask user for the value of each cell
                    grid[i].append(val) # add that value to the grid
            gridFilled = True # once done the grid is filled
        print("")
        print("The Current Board:")
        printGrid(grid) # printing current board given by the user
        print("")
        print("The Solved Board:")
        backtracking(grid) # solve the board
        printGrid(grid) # print the solved board

if __name__ == "__main__": # main method
    main()
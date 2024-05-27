import string
import random

# Create the grid
grid = []
for i in range(10):
    row = []
    for j in range(10):
        row.append(" ")
    grid.append(row)

# Add row and column names
for i in range(10):
    grid[i].insert(0, str(i))
    grid[i].append(str(i))
grid.insert(0, list("  " + string.ascii_uppercase[:10] + " "))
grid.append(list("  " + string.ascii_uppercase[:10] + " "))

# Set up the mines
num_mines = 10
mines = random.sample([(i, j) for i in range(10) for j in range(10)], num_mines)
for mine in mines:
    i, j = mine
    grid[i+1][j+1] = "*"

# Set up the adjacent mine numbers
for i in range(1, 11):
    for j in range(1, 11):
        if grid[i][j] == " ":
            count = 0
            for row in range(i-1, i+2):
                for col in range(j-1, j+2):
                    if grid[row][col] == "*":
                        count += 1
            if count > 0:
                grid[i][j] = str(count)

# Display the grid
def display_grid():
    for row in grid:
        print("".join(row))

# Game loop
while True:
    display_grid()
    move = input("Enter your move (e.g. R1A, F2B): ")
    move_type = move[0]
    i = int(move[1])
    j = string.ascii_uppercase.index(move[2])

    if move_type == "F":
        if grid[i+1][j+1] == " ":
            grid[i+1][j+1] = "F"
        elif grid[i+1][j+1] == "F":
            grid[i+1][j+1] = " "
    elif move_type == "R":
        if (i, j) in mines:
            print("Game over!")
            display_grid()
            break
        elif grid[i+1][j+1] == " ":
            stack = [(i+1, j+1)]
            while stack:
                i, j = stack.pop()
                if grid[i][j] == " ":
                    grid[i][j] = "R"
                    for row in range(i-1, i+2):
                        for col in range(j-1, j+2):
                            if grid[row][col] == " " and (row, col) not in stack:
                                stack.append((row, col))
        else:
            grid[i+1][j+1] = "R"

    # Check if the user has won
    if all(grid[i+1][j+1] == "F" for i, j in mines):
        print("You win!")
        display_grid()
        break

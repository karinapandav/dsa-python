def dfs(grid, row, col):
    if row < 0 or col < 0:
        return
    elif row >= len(grid) or col >= len(grid[0]):
        return
    elif grid[row][col] == 0:
        return 

    grid[row][col] = 0
    dfs(grid,row - 1,col) 

    dfs(grid,row + 1,col)

    dfs(grid,row,col + 1)
    
    dfs(grid,row,col - 1)          


def num_islands(grid):
    count = 0
    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            if grid[row][col] == 1:
                count += 1
                dfs(grid, row, col)
    return count
print(num_islands([[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]))        
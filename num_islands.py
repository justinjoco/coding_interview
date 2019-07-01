"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

Algorithm:
Get the number of rows and columns
Initialize number of islands as 0
For each point in the grid:
    If point value is '1':
        Increment number of islands
        Do DFS at this point

DFS
    Stop iterating if checked point coords are outside the bounds of the grid or the point's value is 0
    Change this point's value as '0'
    Do this again on each vertical and horizontal neighbor of this point

Notes:
Given grid doubles as a "visited" grid 

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if (grid == None) or len(grid) == 0:
            return 0
        
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_islands = 0
        for row in range(num_rows):
            for column in range(num_cols):
                if grid[row][column] == '1':
                    num_islands+=1
                    self.dfs(grid, row, column, num_rows, num_cols)
        
        
        return num_islands
    
    
    def dfs(self, grid, row, col,num_rows, num_cols):
        if row < 0 or col < 0 or row >= num_rows or col >= num_cols or grid[row][col] == '0':
            return
        
        grid[row][col] = '0'
        self.dfs(grid, row+1,col, num_rows, num_cols)
        self.dfs(grid, row-1,col, num_rows, num_cols)
        self.dfs(grid, row,col+1, num_rows, num_cols)
        self.dfs(grid, row,col-1, num_rows, num_cols)
        
        
        
        
        
        
        
        
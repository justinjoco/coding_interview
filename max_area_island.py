"""
Max Area of Island

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.


Algorithm:
For each element in the grid,
    Do a DFS and keep updating max area with the highest area if the grid element in True

DFS:
    If the grid element is within the bounds and hasn't been visited:
        Conduct a DFS on each of element's neighbors. Accumulate the sum of the neighbors' DFS's + 1
    Otherwise, 
        Return 0
"""


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or grid == None:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        max_area = 0    
        
        def dfs(row, column, num_rows, num_cols, grid):
            if row < 0 or column < 0 or row >=num_rows or column >= num_cols or not grid[row][column]:
                return 0

            grid[row][column] = 0
        
            return 1 + dfs(row - 1, column, num_rows, num_cols, grid) + dfs(row + 1, column, num_rows, num_cols, grid) + dfs(row, column - 1, num_rows, num_cols, grid) + dfs(row, column + 1, num_rows, num_cols, grid)
        
        
        for row in range(num_rows):
            for column in range(num_cols):
                if grid[row][column]:
                    max_area = max(max_area, dfs(row, column, num_rows, num_cols, grid))
                    
                    
                    
       
        return max_area
        
        
    
        
        
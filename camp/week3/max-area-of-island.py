from ast import List


class Solution:
    def dfs(self, grid, row, col):
        grid[row][col] = 2
        summ = 0
        for i in range(4):
            newRow, newCol = self.DIR[i] + row, self.DIR[i+1] + col
            if self.inBound(newRow, newCol) and grid[newRow][newCol] == 1:
                summ += self.dfs(grid, newRow, newCol)

        return summ + 1
                
        
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.DIR = (0,1,0,-1,0)
        self.inBound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        self.maxArea = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    new = self.dfs(grid, row, col)
                    self.maxArea = max(self.maxArea, new)
        
        return self.maxArea 
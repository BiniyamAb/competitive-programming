from ast import List

class Solution:
    def dfs(self, grid, row, col, control):
        self.visited.add((row, col))
        for i in range(4):
            newRow, newCol = self.DIR[i] + row, self.DIR[i+1] + col
            if self.inBound(newRow, newCol) and grid[newRow][newCol] == 1 and (newRow, newCol) not in self.visited:
                 self.dfs(grid, newRow, newCol, control)
        if control:
            self.count += 1
            
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.DIR = (-1,0,1,0,-1)
        self.visited = set()
        self.count = 0
        m = len(grid)
        n = len(grid[0])
        self.inBound = lambda row, col: 0 <= row < m and 0 <= col < n
        
         
        for a in range(n):
            if (0,a) not in self.visited and grid[0][a] == 1:  
                self.dfs(grid, 0, a, False)
        for b in range(m):
            if (b,0) not in self.visited and grid[b][0] == 1: 
                self.dfs(grid, b, 0, False)
        for c in range(n):
            if (m-1,c) not in self.visited and grid[m-1][c] == 1: 
                self.dfs(grid, m-1, c, False)
        for d in range(m):
            if (d,n-1) not in self.visited and grid[d][n-1] == 1: 
                self.dfs(grid, d, n-1, False)
        
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1 and (row, col) not in self.visited:
                    self.dfs(grid, row, col, True)
                    
        return self.count
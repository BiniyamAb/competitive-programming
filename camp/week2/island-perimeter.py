from ast import List

class Solution:
    def dfs(self, grid, row, col):
        self.visited.add((row, col))
        for i in range(4):
            newRow, newCol = row + self.DIR[i], col + self.DIR[i+1]
            if self.inBound(newRow, newCol) and grid[newRow][newCol] == 1 and (newRow, newCol) not in self.visited:
                self.dfs(grid, newRow, newCol)
            elif (newRow, newCol) in self.visited:
                pass
            else:
                self.count += 1
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.count = 0
        self.DIR = (0,1,0,-1,0)
        self.visited = set()
        self.inBound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        control = False
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    vertex = (i,j)
                    control = True
                    break
            if control: break
        
        self.dfs(grid, vertex[0], vertex[1])
        return self.count
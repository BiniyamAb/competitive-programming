from ast import List

class Solution:
    def dp(self, grid, row, col, memo):
        if not self.inBound(row+1, col) and not self.inBound(row, col+1): return grid[row][col]
        if memo.get((row, col)) is not None: return memo[(row, col)]
        if self.inBound(row+1, col):
            bottom = self.dp(grid, row+1, col, memo)
        else:
            bottom = float("inf")
        
        if self.inBound(row, col+1):
            right = self.dp(grid, row, col+1, memo)
        else:
            right = float("inf")
        memo[(row, col)] = min(right, bottom) + grid[row][col]
        
        return memo[(row, col)]
        
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        self.inBound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0]) 
        return self.dp(grid, 0, 0, memo)
        
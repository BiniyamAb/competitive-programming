from ast import List

class Solution:
    
    def dfs(self, board, row, col, change):
        self.visited.add((row, col))
        for i in range(4):
            newRow, newCol = self.DIR[i] + row, self.DIR[i+1] + col
            if self.inBound(newRow, newCol) and board[newRow][newCol] == 'O' and (newRow, newCol) not in self.visited:
                 self.dfs(board, newRow, newCol, change)
        if change:
            board[row][col] = 'X'
        
                
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.DIR = (-1,0,1,0,-1)
        self.visited = set()
        m = len(board)
        n = len(board[0])
        self.inBound = lambda row, col: 0 <= row < m and 0 <= col < n
        
         
        for a in range(n):
            if (0,a) not in self.visited and board[0][a] == 'O':  
                self.dfs(board, 0, a, False)
        for b in range(m):
            if (b,0) not in self.visited and board[b][0] == 'O': 
                self.dfs(board, b, 0, False)
        for c in range(n):
            if (m-1,c) not in self.visited and board[m-1][c] == 'O': 
                self.dfs(board, m-1, c, False)
        for d in range(m):
            if (d,n-1) not in self.visited and board[d][n-1] == 'O': 
                self.dfs(board, d, n-1, False)
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == 'O' and (row, col) not in self.visited:
                    self.dfs(board, row, col, True)
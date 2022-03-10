class Solution:
    def dp(self, n, memo):
        if n == 1: return 1
        if n == 0: return 0
        if memo.get(n-1) is None:
            n1 = self.dp(n-1, memo)
            memo[n-1] = n1
        else:
            n1 = memo[n-1]
            
        if memo.get(n-2) is None:
            n2 = self.dp(n-2, memo)
            memo[n-2] = n2
        else:
            n2 = memo[n-2]
        
        return n1 + n2
        
    def fib(self, n: int) -> int:
        memo = {}
        return self.dp(n, memo)
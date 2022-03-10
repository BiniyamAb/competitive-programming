from ast import List

class Solution:
    def dp(self, cost, i, memo):
        if not self.inBound(i): return 0
        if memo.get(i+1) is None:
            one = self.dp(cost, i+1, memo)
            memo[i+1] = one
        else:
            one = memo[i+1]
        if memo.get(i+2) is None: 
            two = self.dp(cost, i+2, memo)
            memo[i+2] = two
        else:
            two = memo[i+2]

        return min(one, two) + cost[i]
        
        
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        self.inBound = lambda i: 0 <= i < len(cost)
        zeroth = self.dp(cost, 0, memo)
        first = self.dp(cost, 1, memo)
        return min(zeroth, first)
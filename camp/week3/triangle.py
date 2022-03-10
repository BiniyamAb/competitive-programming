from ast import List

class Solution:
    def dp(self, triangle, level, i, memo):
        if not level < len(triangle) or not i < len(triangle[level]) : return 0
        if memo.get((level, i)) is not None:
            return memo[(level, i)]
        one = self.dp(triangle, level+1, i, memo)
        two = self.dp(triangle, level+1, i+1, memo)
        memo[(level, i)] = min(one, two) + triangle[level][i]
        
        return memo[(level,i)]
        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dp(triangle, 0, 0, memo)
from typing import List

class Solution:
    def helper(self, s, e, nums):
        if s - e == 0:
            return nums[s]
        return max(nums[s] - self.helper(s+1, e, nums), nums[e] - self.helper(s, e-1, nums))
    
    def PredictTheWinner(self, nums: List[int]) -> bool:
        res = self.helper(0, len(nums) - 1, nums)
        if res >= 0:
            return True
        return False
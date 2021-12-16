from typing import List

def minPairSum(nums: List[int]) -> int:
    nums.sort()
    maximumPairSum = 0
    j = len(nums) - 1
    for i in range(len(nums)):
        if maximumPairSum < nums[i] + nums[j]:
            maximumPairSum = nums[i] + nums[j]
        j-=1
    
    return maximumPairSum
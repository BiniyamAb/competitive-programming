from collections import defaultdict
from typing import List

def maxOperations(nums: List[int], k: int) -> int:
    count = 0
    freqDict = defaultdict(int)

    for i in range(len(nums)):
        freqDict[nums[i]]+=1
        
    for i in range(len(nums)):
        if freqDict[nums[i]] and freqDict[k - nums[i]]:
            if nums[i] == k - nums[i]:
                if freqDict[nums[i]] < 2:
                    continue
            count+=1
            freqDict[nums[i]] -= 1
            freqDict[k - nums[i]] -= 1
            
    return count

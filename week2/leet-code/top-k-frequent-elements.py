import operator
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    freqDict, res = {}, []
    
    for i in range(len(nums)):
        freqDict[nums[i]] = freqDict.get(nums[i], 0) + 1
    freqDict = dict( sorted(freqDict.items(), key=operator.itemgetter(1),reverse=True))
    lst = list(freqDict.keys())
    
    count = 0
    for val in lst:
        res.append(val)
        count+=1
        if count == k:
            break
    return res
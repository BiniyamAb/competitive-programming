from ast import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 2:
            return [nums[0]]
        freq = Counter(nums)
        lst = []
        for key, v in freq.items():
            lst.append((-v,key))
            
        heapq.heapify(lst)
        elements = []
        for i in range(k):
            tup = heapq.heappop(lst)
            elements.append(tup[1])
        
        return elements
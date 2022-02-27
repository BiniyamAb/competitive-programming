from ast import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        l, r, hInd = 0, length - 1, 0
        while l <= r:
            mid = l + (r-l)//2
            count = length - mid
            if count <= citations[mid]:
                hInd = count
                r = mid - 1
            else:
                l = mid + 1
        
        return hInd
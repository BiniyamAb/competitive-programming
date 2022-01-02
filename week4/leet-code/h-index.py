from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        count = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if count + 1 <= citations[i]:
                count+=1
            else:
                break
            
        return count
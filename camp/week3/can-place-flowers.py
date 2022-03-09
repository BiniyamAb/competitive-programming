from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        inBound = lambda x: 0 <= x < len(flowerbed)
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if count == n: return True
                if inBound(i+1) and flowerbed[i+1] == 1:
                    continue
                if inBound(i-1) and flowerbed[i-1] == 1:
                    continue
                flowerbed[i] = 1
                count += 1
        
        return count == n
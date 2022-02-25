def isBadVersion(val):
    return val
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r, firstBad = 1, n, 1
        while l<=r:
            mid = l + ((r - l)//2)
            if isBadVersion(mid):
                firstBad = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return firstBad
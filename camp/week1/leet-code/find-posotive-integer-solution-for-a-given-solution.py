from ast import List


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        res = []
        for i in range(1, 1001):
            l, r = 1, 1000
            y = -1
            while l <= r:
                mid = l + (r-l)//2
                if customfunction.f(i,mid) == z:
                    y = mid
                    break
                elif customfunction.f(i,mid) > z:
                    r = mid - 1
                else:
                    l = mid + 1
            
            if not y == -1:
                res.append([i,y])
        
        return res
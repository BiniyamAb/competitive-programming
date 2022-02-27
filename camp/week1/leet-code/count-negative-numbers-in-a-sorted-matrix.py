from ast import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        lst = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                lst.append(grid[i][j])
        lst.sort()
        count = l = 0
        r = len(lst) - 1
        
        while l <= r:
            mid = l + (r-l)//2
            if lst[mid] < 0:
                count = mid + 1
                l = mid + 1
            else:
                r = mid - 1
                
        return count
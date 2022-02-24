from ast import List

class Solution:
    def findPosition(self, nums, target, flag):
        l, r, best = 0, len(nums) - 1, -1
        while l <= r:
            mid = l + ((r-l)//2)
            if nums[mid] == target:
                best = mid
                if flag == 1:
                    r = mid - 1
                elif flag == 2:
                    l = mid+1
            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        return best
        
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.findPosition(nums,target,1)
        end = self.findPosition(nums,target,2)
        return [start,end]
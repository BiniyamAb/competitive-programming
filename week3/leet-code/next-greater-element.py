from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monoStack = []
        dic = {}
        lst = []
        for i in range(len(nums2)):
            if i == 0:
                monoStack.append(nums2[i])
                continue
                
            
            num = nums2[i]
            while len(monoStack) > 0 and num > monoStack[-1]:
                dic[monoStack[-1]] = num
                monoStack.pop()
                
            monoStack.append(nums2[i])
            
        if len(monoStack) > 1:
            for i in range(len(monoStack)):
                dic[monoStack[i]] = -1
        else:
            dic[monoStack.pop()] = -1
        
        for i in range(len(nums1)):
            lst.append(dic[nums1[i]])
        
        return lst
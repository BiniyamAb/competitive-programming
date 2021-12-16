from typing import List

def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    m = len(l)
    answer = [False] * m
    for i in range(m):
        lst = nums[l[i]:(r[i] + 1)]
        lst.sort()
        diff = lst[1] - lst[0]
        arithmetic = True
        for j in range(1, len(lst)):
            if lst[j] - lst[j - 1] != diff:
                arithmetic = False
                break
        answer[i] = arithmetic
    
    return answer
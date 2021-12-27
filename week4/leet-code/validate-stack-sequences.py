from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = [pushed[0]]
        pu = 1
        po = 0
        for _ in range((2*len(pushed)) - 1):
            if pu > len(pushed) - 1:
                if popped[po] != stack[-1]:
                    return False
            
            if len(stack) > 0 and popped[po] == stack[-1]:
                stack.pop()
                po+=1
            else:
                stack.append(pushed[pu])
                pu+=1
                
        
        return True
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monoStack = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
        
            while len(monoStack) > 0 and temperatures[i] > temperatures[monoStack[-1]]:
                res[monoStack[-1]] = i - monoStack[-1]
                monoStack.pop()
                
        
        for i in range(len(monoStack)):
            res[monoStack[i]] = 0
        
        return res
            
        
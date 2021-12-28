class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k == len(num):
            return '0'
        stack, count = [], 0
        for i in range(len(num)):
            while len(stack) and count!=k and num[i] < stack[-1]:
                stack.pop()
                count+=1
            stack.append(num[i])
        
        if count!=k:
            while count!=k:
                stack.pop()
                count+=1
        
        stack = "".join(stack)
        stack = int(stack)
        
        return str(stack)
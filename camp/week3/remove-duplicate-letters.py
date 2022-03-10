class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        dic = {}
        for i, string in enumerate(s):
            dic[string] = i
            
        stack = []
        for i in range(len(s)):
            exist = s[i] in stack
            while stack and stack[-1] > s[i] and dic[stack[-1]] > i and not exist:
                stack.pop()
                
            if not exist:
                stack.append(s[i])
        
        
        return "".join(stack)
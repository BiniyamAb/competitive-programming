class Solution:
    def reverseParentheses(self, s: str) -> str:
        lst = []
        if len(s) == 0:
            return ""
        
        for i in range(len(s)):
            
            if s[i] in ")}]":
                j = len(lst) - 1
                temp_lst = []
                while lst[j] not in "({[" and len(lst) > 0:
                    temp_lst.append(lst[-1])
                    lst.pop()
                    j-=1
                 
                lst.pop()
                for val in temp_lst:
                    lst.append(val)
                    
            else:
                lst.append(s[i])
        
        return "".join(lst)
                
        
        
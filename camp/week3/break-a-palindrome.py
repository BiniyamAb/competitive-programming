class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1: return ""
        palindrome = list(palindrome)
        odd = not len(palindrome) % 2 == 0
        mid = len(palindrome) // 2
        
        for i in range(len(palindrome)):
            if odd and i == mid:
                break
            if palindrome[i] != 'a':
                palindrome[i] = 'a'
                return "".join(palindrome)
            
        palindrome[-1] = 'b'
        return "".join(palindrome)
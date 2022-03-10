from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque([])
        dire = deque([])
        n = len(senate)
        
        for i, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r > d:
                dire.append(d+n)
            else:
                radiant.append(r+n)
        
        return "Radiant" if radiant else "Dire"
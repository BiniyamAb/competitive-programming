from typing import List

def maxCoins(piles: List[int]) -> int:
    piles.sort()
    j = len(piles) - 1
    maximum = 0
    for i in range(int(len(piles) / 3)):
        maximum += piles[j - 1]
        j-=2
    
    return maximum

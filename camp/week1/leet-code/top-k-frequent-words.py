from ast import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        lst, lst2 = [], []
        for key, v in freq.items():
            lst.append((-v, key))
        heapq.heapify(lst)
        for i in range(k):
            tup = heapq.heappop(lst)
            lst2.append(tup[1])
        
        return lst2
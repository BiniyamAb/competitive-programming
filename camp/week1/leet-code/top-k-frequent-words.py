from ast import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        lst, lst2, lst3 = [], [], []
        for key, v in freq.items():
            lst.append((-v, key))
        heapq.heapify(lst)
        prev = lst[0][0]
        for i in range(k):
            tup = heapq.heappop(lst)
            if tup[0] == prev:
                lst2.append(tup[1])
            else:
                lst2.sort()
                for i in range(len(lst2)):
                    lst3.append(lst2[i])
                prev = tup[0]
                lst2 = [tup[1]]
                
        lst2.sort()
        for i in range(len(lst2)):
            lst3.append(lst2[i])
        
        return lst3
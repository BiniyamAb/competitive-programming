from collections import Counter
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        lst = []
        for k, v in count.items():
            lst.append((-v,k))
        heapq.heapify(lst)
        lst2 = []
        while len(lst) > 0:
            tup = heapq.heappop(lst)
            lst2.append((-tup[0]) * tup[1])
        
        return "".join(lst2)
        
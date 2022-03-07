from ast import List
from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        steps = 0
        dic = {}
        for i in range(len(arr)):
            if dic.get(arr[i]):
                dic[arr[i]].append(i)
            else:
                dic[arr[i]] = [i]
        
        inBound = lambda i: 0 <= i < len(arr)
        lastIndex = len(arr) - 1
        queue = deque([0])
        visited = set()
        while queue:
            levelSize = len(queue)     
            for i in range(levelSize):
                curr = queue.popleft()
                if curr == lastIndex:
                    return steps
                visited.add(curr)
                if inBound(curr + 1) and not curr + 1 in visited: queue.append(curr + 1)
                if inBound(curr - 1) and not curr - 1 in visited: queue.append(curr - 1)
                lst = dic[arr[curr]]
                if lst:
                    for i in range(len(lst)):
                        if lst[i] not in visited: queue.append(lst[i])
                dic[arr[curr]] = None
            
            steps+=1
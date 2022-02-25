from ast import List
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(arr) == k:
                    heapq.heappushpop(arr, -matrix[i][j])
                    continue
                heapq.heappush(arr, -matrix[i][j])
        
        return -arr[0]
import heapq

class MedianFinder:
    
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        if not self.minHeap:
            heapq.heappush(self.minHeap, num)
        elif not self.maxHeap:
            newNum = -heapq.heappushpop(self.minHeap, num)
            heapq.heappush(self.maxHeap, newNum)
        elif len(self.maxHeap) == len(self.minHeap):
            newNum = -heapq.heappushpop(self.minHeap, num)
            heapq.heappush(self.maxHeap, newNum)
        else:
            newNum = -heapq.heappushpop(self.maxHeap, -num)
            heapq.heappush(self.minHeap, newNum)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
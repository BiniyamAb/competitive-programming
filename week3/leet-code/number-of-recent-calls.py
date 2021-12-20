class RecentCounter:

    def __init__(self):
        self.recentRequests = []
        self.i = 0
    def ping(self, t: int) -> int:
        self.recentRequests.append(t)   
        t2 = t - 3000
        count = len(self.recentRequests) - self.i
        
        while self.recentRequests[self.i] < t2:
            count-=1
            self.i+=1
        
        return count
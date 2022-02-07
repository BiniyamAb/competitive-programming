class Solution:
    def helper(self, friends, k, head):
        if len(friends) == 1:
            return friends[0]
        ind = head + (k - 1)
        ind%= len(friends)
        friends.pop(ind)
        head = ind % len(friends)
        return self.helper(friends, k, head)
        
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1,n+1))
        return self.helper(friends, k, 0)
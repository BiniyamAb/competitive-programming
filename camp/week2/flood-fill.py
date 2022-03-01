from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.visited.add((sr,sc))
        lst = []
        if sc + 1 <= len(image[sr]) - 1:
            lst.append((sr, sc + 1))
        if sc - 1 >= 0:
            lst.append((sr, sc - 1))
        if sr - 1 >= 0:
            lst.append((sr - 1, sc))
        if sr + 1 <= len(image) - 1:
            lst.append((sr + 1, sc))
        
        for i in range(len(lst)):
            if lst[i] not in self.visited and image[sr][sc] == image[lst[i][0]][lst[i][1]]:
                self.floodFill(image, lst[i][0], lst[i][1], newColor)
        
        image[sr][sc] = newColor
        return image